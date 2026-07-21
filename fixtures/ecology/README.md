# Ecology fixtures

> **One-line purpose.** `fixtures/ecology/` holds small, synthetic, public-safe examples that intentionally exercise ecological behavior across more than one KFM domain without becoming a new domain, a truth store, or a publication surface.

**Path:** `fixtures/ecology/`  
**Authority level:** implementation-supporting fixture directory under the canonical `fixtures/` responsibility root  
**Document status:** draft, repository-grounded directory README  
**Truth posture:** cite-or-abstain; fixture behavior is illustrative until a named consumer and executable check verify it  
**Last reviewed:** 2026-07-21

## Quick navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [Repository fit](#repository-fit)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Cross-domain ownership model](#cross-domain-ownership-model)
- [Directory map](#directory-map)
- [Fixture design contract](#fixture-design-contract)
- [Scenario and outcome matrix](#scenario-and-outcome-matrix)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Maintenance and correction](#maintenance-and-correction)
- [Related folders and doctrine](#related-folders-and-doctrine)
- [ADRs](#adrs)
- [Verification status](#verification-status)

## Purpose

Use this directory for bounded ecology examples whose value comes from exercising a relationship across domain boundaries, such as:

- Habitat context joined to a public-safe Flora or Fauna derivative;
- Habitat and Hydrology context shown together in a governed map or Evidence Drawer example;
- synthetic ecological source-role conflicts or missing-evidence states;
- public-safe generalization, denial, hold, abstention, correction, or rollback scenarios that span multiple domain lanes;
- renderer, governed-API, Evidence Drawer, Focus Mode, or documentation examples that cannot be owned accurately by one domain fixture lane.

This directory is a **cross-domain fixture boundary**, not a canonical Ecology domain. When one domain clearly owns an object, source family, policy context, or expected output, place the fixture under `fixtures/domains/<domain>/` instead.

## Authority level

`fixtures/ecology/` is **implementation-supporting and non-authoritative**.

It may demonstrate intended behavior, but it does not define or prove:

- object meaning;
- machine shape;
- source authority;
- evidence closure;
- policy approval;
- review approval;
- release state;
- publication authority;
- public map or API truth;
- AI authority;
- implementation completeness.

Authority remains separated by responsibility root:

| Concern | Owning root | Fixture relationship |
|---|---|---|
| Human doctrine and domain boundaries | `docs/` | This README cites and applies those boundaries. |
| Object meaning | `contracts/` | Fixtures may illustrate contracts but do not define them. |
| Machine shape | `schemas/` | Fixtures may exercise schemas but do not establish schema authority. |
| Allow, deny, restrict, hold, or abstain rules | `policy/` | Fixtures may model policy inputs and expected outcomes only. |
| Runtime or regression enforcement | `tests/`, validators under `tools/` | A named consumer must verify the fixture before behavior is called implemented. |
| Lifecycle data | `data/` | Fixtures are never RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data. |
| Receipts and proofs | governed receipt and proof homes | Toy receipt-shaped or proof-shaped examples are not actual receipts or proofs. |
| Release decisions | `release/` | Fixtures cannot promote, publish, correct, withdraw, or roll back a real release. |

## Status

| Surface | Status | Evidence-bounded interpretation |
|---|---|---|
| Directory path | **CONFIRMED** | `fixtures/ecology/README.md` exists on the inspected base commit. |
| This README | **CONFIRMED file / draft guidance** | Revised in place as the directory boundary and routing document. |
| Parent fixture boundary | **CONFIRMED** | `fixtures/README.md` distinguishes runtime and synthetic fixtures from lifecycle data, generated artifacts, and test-only fixtures. |
| Adjacent Habitat, Flora, and Fauna fixture roots | **CONFIRMED** | Their directory READMEs exist and document domain-specific fixture ownership. |
| Child files or child directories directly under `fixtures/ecology/` | **UNKNOWN** | No complete non-truncated directory listing was available in this update. Do not infer payload presence from this README. |
| Named ecology validator or test consumer on the inspected base | **NEEDS VERIFICATION** | No current executable consumer was verified for this directory. |
| Repository-wide validator entry point | **CONFIRMED placeholder only** | `tools/validate_all.py` exists but contains placeholder prose rather than an executable validation suite at the inspected base. |
| CI execution, required checks, or branch protection | **UNKNOWN** | Workflow documentation exists, but current run results and required-check settings were not established by this README update. |

## Repository fit

Directory Rules place synthetic, golden, valid, and invalid examples under the canonical `fixtures/` responsibility root. They also require cross-domain material to remain under the lowest common responsibility root instead of being forced into an arbitrary domain lane.

The relationship is:

```text
fixtures/
├── README.md                 # parent fixture boundary
├── ecology/
│   └── README.md             # this cross-domain routing boundary
└── domains/
    ├── habitat/              # domain-owned Habitat examples
    ├── flora/                # domain-owned Flora examples
    └── fauna/                # domain-owned Fauna examples
```

The tree above shows only paths verified for this README update. It does not assert a complete recursive inventory.

### `fixtures/` versus `tests/fixtures/`

Use `fixtures/ecology/` for reusable runtime, documentation, renderer, governed-API, and cross-domain synthetic examples. Use `tests/fixtures/` for deterministic test-only inputs when the repository's test structure owns the fixture exclusively.

Do not duplicate the same fixture in both homes without a documented canonical source and synchronization rule.

## What belongs here

This directory may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy cross-domain references among Habitat, Flora, Fauna, Hydrology, Soil, Hazards, Agriculture, or map/UI contexts;
- synthetic source-role, evidence, rights, sensitivity, policy, review, freshness, release, correction, and rollback states;
- public-safe generalized geometry or intentionally geometry-free cases;
- paired synthetic input and expected-output examples;
- finite outcome examples such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` when the expected reason is explicit;
- README files that document a bounded child fixture family, its owner, consumer, expected outcome, and verification state.

A fixture belongs here only while its **cross-domain nature is essential**. Stable domain-owned examples should move to the owning domain fixture lane.

## What does not belong here

Do not place any of the following under `fixtures/ecology/`:

- real source records, live upstream payloads, source exports, scraped material, or field observations;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data;
- authoritative taxonomic, occurrence, habitat, hydrologic, soil, hazard, agriculture, or land records;
- actual `SourceDescriptor`, `EvidenceBundle`, `RunReceipt`, proof pack, `PolicyDecision`, review record, release manifest, rollback card, correction notice, or withdrawal notice;
- contracts, schemas, policy rules, validator implementation, connector code, pipeline code, application code, or release tooling;
- public API material, public map material, public tiles, direct model output, or published artifacts;
- credentials, private data, restricted source content, protected exact locations, or reconstructive clues that could expose sensitive ecological information;
- a second canonical home for any schema, contract, policy, source, registry, receipt, proof, release, catalog, or publication object.

If a file is real, sensitive, rights-unclear, or lifecycle-bearing, remove it from the fixture path and route it through the governed intake or quarantine process.

## Inputs

Accepted inputs are intentionally bounded:

- manually authored synthetic scenarios;
- public-safe toy geometry created specifically for testing or documentation;
- minimized and transformed examples whose source material is no longer present and whose transformation is documented;
- expected-output pairs derived from an agreed contract, schema, policy, validator, renderer, or governed-API behavior;
- cross-domain scenario definitions supplied by maintainers or reviewers.

Each stable fixture should identify, in the file or its child README:

1. whether it is entirely synthetic;
2. the scenario owner or owning domains;
3. its intended consumer;
4. its expected outcome;
5. any public-safety transform applied;
6. the evidence, policy, review, release, correction, and rollback states it is designed to exercise.

Do not copy real records into this lane merely to make a fixture realistic.

## Outputs

This directory may support downstream:

- contract and schema checks;
- policy dry-runs;
- validator and regression tests;
- governed-API dry-runs;
- MapLibre renderer checks;
- Evidence Drawer examples;
- Focus Mode finite-outcome examples;
- documentation and review examples;
- correction and rollback drills;
- expected-output comparisons.

A fixture output remains an example. A passing consumer does not, by itself, prove source admissibility, evidence closure, public safety, release readiness, publication, or system-wide correctness.

## Cross-domain ownership model

KFM domain boundaries must remain visible inside a cross-domain fixture.

| Information represented | Owning lane | Ecology fixture rule |
|---|---|---|
| Habitat patch, land cover, ecological system, suitability, connectivity, restoration opportunity | Habitat | May be the context backbone; must remain modeled or observed according to its source role. |
| Plant taxon, specimen, plant occurrence, rare-plant or vegetation-community record | Flora | Reference only through a synthetic or public-safe Flora-shaped object; do not transfer Flora authority to Habitat. |
| Animal taxon, occurrence, seasonal range, mortality, disease, or sensitive-species record | Fauna | Use toy or generalized data; preserve geoprivacy and deny reconstructive detail. |
| Watershed, stream, wetland hydrology, gauge, or water observation | Hydrology | Use as context through explicit references; Habitat does not become hydrologic truth. |
| Soil map unit, component, horizon, or property | Soil | Use as substrate context only; retain Soil ownership. |
| Hazard observation, model, warning context, exposure, or resilience indicator | Hazards | Keep observed, modeled, regulatory, and operational roles distinct. |
| Cross-domain relationship or composite public-safe presentation | The responsibility root that owns the artifact | `fixtures/ecology/` may hold the synthetic example when no single domain can own it accurately. |

### Source-role anti-collapse

Keep source roles explicit. A modeled suitability surface is not an occurrence. A habitat context layer is not a regulatory designation. A generalized derivative is not the exact source record. A rendered map feature is not evidence authority.

## Directory map

At the inspected base, this README is the only path under `fixtures/ecology/` verified in this update.

Do not add a child directory merely because a scenario is ecological. Add one only when:

- multiple related fixtures share one bounded purpose;
- the child has a clear owner and consumer;
- the expected outcomes are documented;
- the child README preserves this directory's non-authoritative posture;
- a domain-specific lane would be less accurate.

Recommended child names, when evidence supports creating them, should describe the scenario rather than inventing a new authority family. Examples include `habitat_flora_join/`, `habitat_hydrology_context/`, `public_safe_overlay/`, or `golden/`. These names are examples, not claims that the directories exist.

## Fixture design contract

A reviewable ecology fixture should follow these rules:

1. **Synthetic by default.** Use toy identifiers, toy taxa, toy sources, toy timestamps, toy hashes, and toy geometry.
2. **Small and deterministic.** Keep files compact enough for ordinary code review and reproducible without a live network.
3. **Ownership visible.** Identify which domain owns every consequential object or assertion.
4. **Source role visible.** Preserve observed, modeled, regulatory, aggregate, administrative, candidate, or synthetic posture where material.
5. **State dimensions separated.** Schema validity, semantic validity, evidence resolution, citation validity, rights, sensitivity, policy, review, freshness, release, renderer safety, correction, rollback, and expected output are separate checks.
6. **Expected outcome explicit.** State the expected finite outcome and reason code or failure class when the consumer contract supports one.
7. **Public safety first.** Prefer no geometry; otherwise use clearly toy or generalized geometry that cannot expose protected details.
8. **Input and output paired.** Pair stable inputs with expected outputs when practical.
9. **Consumer linked.** Do not call a fixture verified until its exact validator, test, renderer check, governed-API dry-run, or documentation consumer is identified.
10. **No authority upgrade.** A fixture never becomes evidence, policy, review, release, or publication authority by repetition or test success.

### Suggested naming

Use names that reveal both scenario and role:

```text
<scenario>.input.json
<scenario>.expected.json
<scenario>.valid.json
<scenario>.invalid.json
<scenario>.geojson
<scenario>.md
```

Avoid names such as `final.json`, `real.json`, `production.json`, or `authoritative.json` in this fixture lane.

## Scenario and outcome matrix

| Scenario | Expected posture | Preferred location |
|---|---|---|
| Habitat-only land-cover or ecoregion example | Valid, invalid, expected output, or watcher scenario | `../domains/habitat/` |
| Flora-only occurrence, taxon, phenology, source, or public-safe plant derivative | Valid, generalized, denied, or review-required | `../domains/flora/` |
| Fauna-only occurrence, range, stale-source, or sensitive-denial example | Valid, generalized, `DENY`, `ABSTAIN`, or review-required | `../domains/fauna/` |
| Habitat × Flora synthetic context join | Context-only, evidence-resolved, or review-required | This directory until ownership becomes clear. |
| Habitat × Fauna public-safe proof-support example | Proof-support, generalized, denied, or review-ready | Prefer Habitat's existing thin-slice lane when it owns the scenario. |
| Habitat × Hydrology wetland or watershed context | Context-only, bounded `ANSWER`, or `ABSTAIN` | This directory or the Hydrology fixture lane, according to ownership. |
| Ecology × Hazards overlay | Context-only, stale, modeled, denied, or review-required | This directory when the combined presentation is the subject. |
| Missing evidence or unresolved citation | `ABSTAIN` | This directory or the owning domain's invalid lane. |
| Rights or sensitivity unresolved | `DENY`, hold, or quarantine-required | Owning domain invalid lane when possible; this directory only for cross-domain behavior. |
| Consumer or validator fails unexpectedly | `ERROR` | Pair the input with an expected failure artifact only after the failure contract is defined. |
| Stable cross-domain expected output | Deterministic expected output, never release state | A verified child `golden/` lane or a documented sibling pair. |

## Validation

### Required content checks

Before accepting a fixture or README change, verify:

- the file is synthetic or demonstrably public-safe;
- no credentials, private data, real source payload, protected location, or reconstructive clue is present;
- the path is correct for the artifact's primary responsibility;
- a domain-specific fixture lane is not the more accurate owner;
- source role, evidence state, rights state, sensitivity state, review state, release state, correction state, and expected outcome are explicit where material;
- JSON, GeoJSON, YAML, Markdown, or other syntax is valid for the file type;
- stable inputs and expected outputs agree;
- relative links in README files resolve;
- the named consumer exists and exercises the intended success or failure path;
- no fixture is described as proof of publication, source authority, or implementation completeness.

### Repository-native validation posture

No executable repository-wide validation command was confirmed for this lane at the inspected base. `tools/validate_all.py` is present only as a placeholder, so this README intentionally does not publish a command that would imply working validation.

When an ecology fixture consumer is implemented, document its exact repository path and supported command here. Keep live-network checks separate from the no-network default.

### What a passing check does not prove

A passing fixture check proves only the behavior exercised by that check against those inputs. It does not prove:

- source accuracy or currency;
- rights or redistribution permission;
- absence of sensitive joins outside the fixture;
- policy completeness;
- EvidenceBundle closure for real claims;
- release approval;
- public safety of unrelated records;
- production runtime or deployment behavior.

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life` at the inspected base. CODEOWNERS is a review-routing mechanism, not proof that review occurred or that policy-significant separation of duties was satisfied.

Additional review should be requested when a change affects:

- **domain meaning:** the owner of every affected domain lane;
- **sensitivity or geoprivacy:** the relevant policy or sensitivity reviewer;
- **rights or source terms:** a source or rights reviewer;
- **finite outcomes or public behavior:** governed-API, Evidence Drawer, Focus Mode, or UI maintainers;
- **release, correction, or rollback semantics:** release-governance reviewers.

Do not encode unverified role names or teams as executable CODEOWNERS entries.

## Maintenance and correction

- Update this README when verified child lanes, payload families, consumers, expected-output conventions, or validation commands change.
- Keep child READMEs synchronized with this boundary.
- Move stable domain-owned fixtures into `fixtures/domains/<domain>/` and update inbound links in the same change.
- Record a canonical source and synchronization rule before mirroring a fixture into `tests/fixtures/` or another compatibility location.
- Keep files small enough for ordinary review unless an explicit large-fixture storage decision exists.
- Remove stale examples when their contract or consumer is retired, while preserving useful lineage in commit history or an approved deprecation note.
- If real or sensitive material is discovered, stop using the fixture, remove it from ordinary review surfaces, route it to quarantine or the proper authority root, and record the correction path.

### Rollback

For a documentation-only mistake, revert the README commit or restore the previous content on the review branch. For a fixture mistake, revert the fixture and any paired output together. Do not delete a public correction history or pretend a sensitive-data incident was merely a documentation typo.

## Related folders and doctrine

Verified related files and lanes at the inspected base:

- [`../README.md`](../README.md) — parent runtime and synthetic fixture boundary.
- [`../domains/habitat/README.md`](../domains/habitat/README.md) — Habitat-owned fixture lane.
- [`../domains/flora/README.md`](../domains/flora/README.md) — Flora-owned fixture lane.
- [`../domains/fauna/README.md`](../domains/fauna/README.md) — Fauna-owned fixture lane.
- [`../../docs/domains/habitat/README.md`](../../docs/domains/habitat/README.md) — Habitat domain boundary and non-ownership rules.
- [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) — canonical placement doctrine.
- [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) — current review-routing evidence.
- [`../../.github/workflows/README.md`](../../.github/workflows/README.md) — workflow authority and verification boundaries.

Other domain lanes such as Hydrology, Soil, Hazards, and Agriculture may participate in cross-domain ecology scenarios, but their exact fixture paths and consumers must be verified before being added as links here.

## ADRs

No target-specific accepted ADR was verified for `fixtures/ecology/` in this update.

This README does not add, remove, rename, or reclassify a canonical root; it does not create a parallel schema, contract, policy, source, registry, receipt, proof, release, catalog, or publication home. Therefore this documentation-only revision does not require a new ADR under the inspected Directory Rules.

A future change requires an ADR or explicit architecture decision when it would:

- create or retire a canonical or compatibility root;
- turn Ecology into a new authority-bearing domain rather than a cross-domain fixture concept;
- create a parallel machine-schema, policy, source, registry, release, receipt, proof, or catalog home;
- change the canonical lifecycle or trust membrane;
- reverse an accepted placement rule.

## Verification status

| Acceptance item | Status | Evidence or limit |
|---|---|---|
| Target file read from immutable base | **PASS** | `fixtures/ecology/README.md` fetched at the pinned base commit. |
| Placement under `fixtures/` | **PASS** | Confirmed against Directory Rules and the parent fixture README. |
| Cross-domain, non-domain posture preserved | **PASS** | Aligned with Directory Rules' cross-domain placement rule and Habitat's explicit non-ownership boundary. |
| Parent fixture relationship | **PASS** | `fixtures/README.md` inspected at the pinned base. |
| Habitat, Flora, and Fauna fixture relationships | **PASS** | Their directory READMEs were inspected at the pinned base. |
| Review route | **PASS** | `.github/CODEOWNERS` routes `/fixtures/` to `@bartytime4life`. |
| Current child inventory under `fixtures/ecology/` | **UNKNOWN** | Complete directory listing was not available through the selected connector operations. |
| Current payload inventory | **UNKNOWN** | No payload file is asserted by this README. |
| Current consumer and validator alignment | **NEEDS VERIFICATION** | No executable ecology consumer was confirmed on the inspected base. |
| Repository-wide validator command | **FAIL as an executable claim** | `tools/validate_all.py` is a placeholder; no command is documented here. |
| CI, workflow-run, and branch-protection enforcement | **NOT RUN / UNKNOWN** | No current run or repository-settings evidence was used. |
| Sensitive-data and rights review of future payloads | **NOT APPLICABLE to this README-only change** | Must be repeated for every added or changed fixture payload. |
