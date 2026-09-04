<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-habitat-readme
title: "configs/domains/habitat/ — Governed Habitat Configuration Boundary"
type: readme
version: v0.5
status: draft
owners: ["OWNER_TBD — Config steward", "OWNER_TBD — Habitat steward", "OWNER_TBD — Consumer owner", "OWNER_TBD — Applicable source, model, sensitivity, validation, policy, release, and documentation reviewers"]
created: 2026-06-16
updated: 2026-09-04
policy_label: "public; non-secret; non-authoritative; landscape-not-species; model-not-observation; fail-closed; no-live-binding; no-source-activation; no-release-authority"
current_path: configs/domains/habitat/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
inherited_parent: configs/domains/README.md
scope_id: kfm://scope/configs/domains/habitat
truth_posture: "CONFIRMED tracked inventory, adopted placement, inspected code and workflow boundaries / PROPOSED future consumer-bound configuration / UNKNOWN operational loading, policy, release, and production behavior / NEEDS VERIFICATION consumer-specific dependencies and historical alias findings"
evidence_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
reconciled_base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
prior_blob: 010b05e30b1d9966cbfe00d87a1b72fcb9872a58
review_route: "@bartytime4life via /configs/ CODEOWNERS; routing is not independent approval"
related: ["configs/domains/README.md", "docs/domains/habitat/README.md", "docs/doctrine/directory-rules.md", "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md", "pipeline_specs/habitat/README.md", "tools/validators/domains/habitat/README.md", ".github/workflows/domain-habitat.yml"]
notes: ["Same-path documentation-only revision; no configuration payload or consumer is added.", "Preserves document identity, prior H2 anchors, and HAB-CFG verification IDs while replacing stale blanket-placeholder claims.", "The two-commit base reconciliation changes only catalog/triplet/README.md; inspected Habitat and governing files are unchanged."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Habitat Domain Configuration

**Configure a verified consumer; never configure truth.**

`configs/domains/habitat/` holds configuration-facing guidance and, when justified, shared non-secret Habitat defaults or templates. It does not own landscape evidence, species records, source admission, policy, or release decisions.

> [!IMPORTANT]
> **Current local inventory: `README.md` and an empty `.gitkeep`.** No tracked executable configuration payload is present. A bounded code search found documentation and historical receipt references, not an executable consumer of this path. This does not prove the absence of ignored, external, dynamically selected, or unindexed consumers.
>
> **The surrounding Habitat lane has mixed maturity, not uniformly placeholder status.** The critical-habitat source-role guard is executable; the domain workflow runs land-cover materiality validation and separate proof/release readiness holds. None of these establishes that this configuration directory is loaded.

[Status](#status) · [Validation](#validation) · [Consumer contract](#minimum-per-file-contract) · [Sensitive joins](#rights-sensitivity-geoprivacy-and-join-induced-risk) · [Open verification](#open-verification-register) · [Evidence](#evidence-ledger)

## Purpose

This child inherits the [domain configuration boundary](../README.md). It explains safe configuration for Habitat processing, presentation, and review without duplicating the [Habitat domain doctrine](../../../docs/domains/habitat/README.md).

Apply adopted Directory Rules §10.4 before adding a file: shared non-secret defaults may belong in `configs/`; a single application's configuration normally follows that application; pipeline run definitions belong in `pipeline_specs/`; deployment wiring belongs in `infra/`; admissibility rules belong in `policy/`. A Habitat topic alone does not justify placement here.

## Authority level

**Configuration support only.** Meaning remains with contracts, machine shape with schemas, admissibility with policy, source identity/admission with source governance, and release decisions with release controls. Configuration may reference those authorities; it cannot acquire or replace them.

Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`. Promotion is a governed transition, not a file move, successful parse, commit, or layer toggle. Public clients use governed APIs and released public-safe artifacts, never this directory as an operational trust API or a shortcut to internal stores.

## Status

Evidence was read at `bb3eb695e6068b38453ca3ded8f1394a8fdebc20` and reconciled to `700570cbcf191038aa20a030174c2dd08cf93675`. The intervening comparison changed only `catalog/triplet/README.md`.

```text
configs/domains/habitat/
├── .gitkeep      # Zero-byte, non-semantic marker
└── README.md     # Configuration boundary; no runtime activation
```

| Surface | Confirmed scope at the evidence pin | What remains unproved |
|---|---|---|
| This directory | Two tracked files; no payload beyond documentation and marker. | Loader, precedence, runtime binding, or external consumers. |
| Critical-habitat role guard | Inspected executable code and seven focused tests; separate regulatory-designation and modeled-suitability pairings. | Real source identity, species presence, rights, policy, or evidence closure. |
| Land-cover materiality | Inspected adapter entry and domain-workflow command bindings; its profile is outside this directory. | This session did not execute that complete fixture family. |
| Habitat validator index | Documents five substantive validators and five remaining placeholders, including the shared-backed EvidenceBundle entrypoint. | This documentation pass did not audit or execute every listed implementation. |
| `domain-habitat` workflow | Runs materiality tests and fixture validation; proof and release jobs execute guards that report explicit holds. | A held green job is not an emitted proof or completed release dry-run. |
| Pipeline-spec index | Documents ten inactive YAML declarations and a separate inactive materiality profile. | Pipeline execution, network permission, source activation, or lifecycle writes. |
| Production and public operation | Not established by this configuration lane. | Deployment, operational geoprivacy, policy enforcement, release, and publication. |

The July v0.4 package, schema, policy, alias, and registry findings remain historical evidence. They are not automatically current, resolved, or applicable to every future consumer.

## What belongs here

Safe configuration-facing documentation, deliberately inactive synthetic examples, and genuinely shared defaults or profile selectors for a named consumer may belong here. A selector can request an already-governed label, caveat, review route, uncertainty display, or public-safe representation; it cannot approve the referenced profile.

**PROPOSED authoring is allowed:** an isolated, reversible template or parser proposal may be developed with explicit unknowns and negative tests. Live-source admission, operational binding, policy approval, and release checks apply to their respective transitions; they are not prerequisites for writing a harmless draft.

## What does NOT belong here

Do not store real observations, occurrences, specimens, patches, sensitive geometry, source captures, model coefficients or training data, model cards, SourceDescriptors, policy rules, schemas, contracts, evidence bundles, receipts, proofs, catalog records, release records, or published artifacts here.

Secrets, credentials, cookies, private endpoints, signed URLs, internal hostnames, workstation-specific paths, and private parcel/person details are prohibited. So are exact or reconstructable nesting, denning, roosting, spawning, refuge, rare-species, restoration, stewardship, cultural, archaeological, or infrastructure-linked locations. Examples must not encode real protected places through plausible identifiers or geometry.

Executable code, tests, fixtures, deployment wiring, and operational pipeline declarations remain in their responsibility-owning lanes. Do not create Habitat-local copies of shared trust objects or revive compatibility paths as new authority.

## Inputs

Before operational use, identify the exact consumer/version and owner; explicit load path; format/parser; config identity/version/digest; schema and semantic references; precedence; and required authority profiles. Include source-role, object-family, spatial support, temporal scope, model limitations, rights, sensitivity, evidence, and release references only where relevant to that consumer's consequence.

Record unresolved dependencies as `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`. Missing support must prevent consequential use, not be silently filled from a filename, a model, a map, or an AI-generated explanation.

## Outputs

The current lane provides documentation only. A future consumer may produce a parse result, validation result, or candidate in its own owning lane; this directory is not an output store.

No config value authorizes a source fetch, model run, policy decision, lifecycle write, evidence assertion, release, public tile, report, or AI answer. A reference to an authority-bearing object is not the decision or proof itself.

## Validation

For a README change, check UTF-8/LF, final newline, metadata, one H1, stable anchors and IDs, balanced fences, resolving local links, absence of conflict markers and sensitive values, and agreement between currentness claims and exact code/workflow evidence. Compare the remote base and head to confirm the intended path-only diff.

The following commands are **verified repository command bindings**, not a generic Habitat-config validation suite. Run from a suitable repository checkout with its declared dependencies:

```bash
# Synthetic critical-habitat source-role guard.
python -m unittest -v tests.domains.habitat.test_critical_habitat_source_role

# Separate land-cover materiality family, bound by domain-habitat.yml.
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose
python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

The [focused source-role workflow](../../../.github/workflows/habitat-critical-habitat-source-role.yml) has path filters that do not include this README. Do not claim it ran because documentation changed. The [domain workflow](../../../.github/workflows/domain-habitat.yml) has broader triggers; hosted results must still be read for the exact head.

**This revision's execution limit:** seven source-role tests passed under Python 3.13.5 in a two-file reconstruction whose validator and test bytes matched their Git blobs. The workflow targets Python 3.11; that interpreter was not available locally. That is bounded test evidence, not a full-checkout run. Materiality, declaration, repository-wide, hosted CI, browser, runtime, deployment, and release checks were not executed by this documentation pass. Use the [pipeline-spec boundary](../../../pipeline_specs/habitat/README.md) for its separate declaration/profile validation families.

A future config consumer needs positive and negative tests for parsing, duplicate and unknown keys, explicit selection, no auto-discovery, precedence conflicts, atomic reload, unsupported versions, denied authority upgrades, sensitive joins, deterministic diagnostics, deactivation, and rollback.

## Review burden

[CODEOWNERS](../../../.github/CODEOWNERS) routes `/configs/` to `@bartytime4life`. That is a verified review route, not an accepted assignment to every steward role or proof of independent approval.

README review needs configuration/documentation and Habitat context. Consumer-bound changes additionally need the affected consumer and applicable source, model, schema, rights, sensitivity, policy, and release reviewers. Unassigned roles remain `OWNER_TBD`; missing independent review must stay visible.

## Related folders

| Responsibility | Navigation |
|---|---|
| Inherited configuration boundary | [Domain configs](../README.md) |
| Habitat meaning and cross-domain ownership | [Habitat domain](../../../docs/domains/habitat/README.md) |
| Inactive pipeline intent, not shared defaults | [Habitat pipeline specifications](../../../pipeline_specs/habitat/README.md) |
| Validator implementation and dependency navigation | [Habitat validator index](../../../tools/validators/domains/habitat/README.md) |
| Source-role implementation | [Validator](../../../tools/validators/domains/habitat/validate_critical_habitat_source_role.py) and [tests](../../../tests/domains/habitat/test_critical_habitat_source_role.py) |
| Materiality implementation | [Adapter](../../../tools/validators/domains/habitat/validate_land_cover_materiality.py) |
| Contribution and review boundaries | [Contributor guide](../../../CONTRIBUTING.md) and [CODEOWNERS](../../../.github/CODEOWNERS) |

For contracts, schemas, policy, fixtures, tests, and release families, follow those owning indexes and verify the actual consumer dependency. This README neither creates a parallel authority map nor treats an index entry as proof of implementation or acceptance.

## ADRs

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts the pinned [Directory Rules v2](../../../docs/doctrine/directory-rules.md) bytes. Their internal draft label is preserved in the adopted artifact; it does not undo that adoption. This same-path revision applies §10.4 configuration ownership and §16.3 `BOUNDARY_COMPACT` inheritance.

No ADR is adopted or amended here. A new authority home, source-role mapping, canonical alias, compatibility retirement, sensitivity rule, or public access path requires its owning decision and, where applicable, migration approval. Do not infer another ADR's acceptance from a domain README's shorthand.

## Last reviewed

**2026-09-04**, at the evidence and reconciled base commits in [Status](#status). Re-review on the first payload or consumer, parser/precedence change, accepted ADR change, source/model/profile change, sensitive join, workflow/validation change, exposure change, correction, withdrawal, or rollback.

The parent README's child-version table is an explicitly pinned older snapshot; this update does not rewrite it or any historical receipt as though they had observed v0.5.

## Bounded context and ubiquitous language

**Habitat is landscape context, not species-record ownership.** Animal occurrences remain Fauna-owned; plant taxa, specimens, and plant occurrences remain Flora-owned. Water, substrate, crop, hazard, archaeology, and people/land evidence retain their source-domain responsibility when joined.

Here, a *configuration* is a consumer input; a *profile reference* selects existing governed meaning; a *validation pass* reports bounded checks; and *deactivation* stops future selection. None is source admission, evidence closure, a designation, or a release decision.

## Configuration classes

Only documentation and the non-semantic directory marker are observed here. Templates, examples, shared defaults, presentation selectors, and compatibility mappings are future classes, not existing payloads.

Classify each proposed file explicitly. Operational selection needs a verified consumer; a template filename, `public: true`, `safe: true`, or `validated: true` cannot confer activation or authority.

## Minimum per-file contract

This is an acceptance checklist, **not a new schema or implemented loader contract**.

| Concern | Required consumer-bound definition |
|---|---|
| Identity | Stable config ID, version, format version, class, digest, status, and owner. |
| Binding | Exact consumer/version, explicit selection mechanism, intended and prohibited uses. |
| Parsing | Encoding, size/depth bounds where relevant, duplicate-key rejection, unknown-key behavior, and unsupported-version failure. |
| Precedence | Declared merge order, override limits, conflict rejection, and atomic load/reload. |
| Authority | Applicable semantic, schema, policy, source, model, sensitivity, and release references; no inline replacement authority. |
| Context | Spatial/temporal support, units, uncertainty, freshness, limitations, and cross-domain ownership. |
| Validation | Synthetic positive/negative fixtures, deterministic output, no-network default, no implicit activation, and safe diagnostics. |
| Recovery | Disable path, known-good version, affected-output inventory, correction/withdrawal refs, invalidation, and rollback/replay tests. |

A compatibility exception to rejecting unknown keys needs explicit scope and tests. Missing safety-significant support cannot fall back to a more permissive profile.

## Consumer binding, precedence, and discovery

No universal Habitat config loader or precedence order is established. Defaults, domain, local, environment, deployment, and runtime inputs must have consumer-specific, tested precedence; this README does not prescribe an unimplemented ordering.

Require explicit selection and atomic application. Directory presence must not trigger discovery or execution. Missing or stale input must leave a safe disabled state, never a partially updated consumer. Overrides cannot weaken source, evidence, rights, sensitivity, policy, review, correction, or release controls.

## Habitat object family boundaries

| Product or context | Preserve | Never infer from it alone |
|---|---|---|
| Land cover / ecological system / HabitatPatch | Classification, scheme/version, scale, support, geometry and uncertainty. | Habitat quality, occupancy, species presence or absence. |
| SuitabilityModel / HabitatQualityScore / UncertaintySurface | Method, inputs, calibration, applicability, units, limitations and uncertainty. | Observation, universal quality, regulatory designation, or model fitness. |
| ConnectivityEdge / Corridor | Nodes, resistance/cost assumptions, method, time and uncertainty. | Observed animal movement, guaranteed passage, or access rights. |
| RestorationOpportunity | Candidate/model status and feasibility limitations. | Approved, funded, prescribed, completed, or successful intervention. |
| StewardshipZone / protected-area context | Administrative identity, effective time and source limitations. | Ownership, title, access permission, ecological condition, or designation authority. |
| Regulatory critical habitat | Issuing record, designation scope, effective time and source role. | Species occurrence, modeled suitability, or KFM legal advice. |
| Occurrence-context join / aggregate / synthetic fixture | Foreign ownership, support unit, suppression, test-only or candidate status. | New occurrence truth, local absence, or production readiness. |

## Source-role vocabulary and anti-collapse

Habitat doctrine describes seven high-level roles: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`. They are not interchangeable. Do not convert these display/domain concepts into a global machine enum by configuration.

The inspected critical-habitat guard uses its own explicit `REGULATORY_CRITICAL_HABITAT` / `REGULATORY` / `DESIGNATION_CONTEXT` and `MODELED_HABITAT` / `MODELED` / `SUITABILITY_MODEL` pairings. That bounded fixture profile is not a universal SourceDescriptor mapping or regulatory source admission.

The v0.4 shared-role vocabulary mismatch remains a **consumer-specific verification item**. Require a versioned accepted mapping wherever a consumer crosses vocabularies; retain original roles and provenance. Unknown mappings fail closed. Derived products receive their own justified role, never an in-place authority upgrade. The current Habitat domain README leaves NWI source-role assignment **NEEDS VERIFICATION**; this config update does not assign it.

## Observation, model, regulatory, and administrative boundaries

Keep source observations, remote-sensing classifications, model estimates, regulatory records, administrative records, aggregates, candidates, and fixtures distinguishable through every consumer. Sensor or classified land cover is not automatically field-observed ecological truth.

Model presentation must preserve model/code/spec version, model-card and run-receipt references, input/covariate versions, calibration/validation scope, thresholds, intended/prohibited uses, applicability, uncertainty, and review. Configuration cannot approve fitness, create a legal designation, turn restoration opportunity into an instruction, or turn a stewardship record into title.

## Spatial support, geometry, scale, and public-safe representation

Preserve CRS and axis order, units, resolution, effective support, geometry/topology, positional and classification uncertainty, raster/resampling meaning, and scale applicability. Thresholds or radii without units and intended use are not safe defaults.

Exact/internal and released public-safe geometries remain distinct. Geoprivacy must be evaluated before public tiles, indexes, exports, or payloads are produced. Low zoom, opacity, hidden attributes, client-side clipping, and map style filters are not protection. Select only accepted transformation profiles; do not invent a jitter radius, simplification, aggregation, or suppression policy here.

## Time, freshness, stale state, and correction

Keep source edition/publication, observation interval, regulatory effective/expiry, model training/run/valid, retrieval, validation/review, release, derivative-build, embargo, supersession, correction, withdrawal, and rollback times distinct where material.

A fresh fetch may contain an old vintage; a new tile may contain stale evidence. Do not relabel partial, delayed, expired, corrected, superseded, withdrawn, or unknown support as current. Preserve that state and use an evidenced alternative or abstain; never fabricate freshness.

## Rights, sensitivity, geoprivacy, and join-induced risk

Operational use must preserve source terms, attribution, redistribution/derivative/AI-use limits, consent or community authority, access, retention, embargo, withdrawal, and review obligations. Unknown, contested, expired, or denied rights block the affected exposure; a public download is not clearance for all uses.

A join inherits at least the strongest applicable restriction and may need stricter handling. Public land cover joined with a restricted occurrence can become restricted; a generalized occurrence joined with a small patch or parcel can become reconstructable. Reassess low counts, repeated queries, differencing, spatial intersections, temporal activity, and cross-layer inference.

Apply governed denial, quarantine, steward-only access, spatial/attribute suppression, aggregation/generalization, temporal delay, and query controls as required. Preserve transformation reasons, receipts, residual risk, and review. Configuration cannot waive these controls or authorize access to protected inputs merely to test them.

## Source registry, connector, and activation boundaries

Reference stable, governed source identities; do not duplicate SourceDescriptors, infer precedence between registry paths, or use a configuration edit to choose a disputed canonical record. The older subtype-first/domain-first finding remains historical until checked for the selected dependency.

A descriptor reference is not activation. Source role, rights, sensitivity, citation, cadence, identity, admission, and current source state stay with source governance. Connectors and watchers may produce candidates and receipts through their own authorized paths; they are non-publishers. This directory grants no live polling, source query, scheduler, or credential access.

## Implementation and governance maturity

Do not repeat v0.4's blanket statements that Habitat validators are placeholders or its CI is TODO-only. The inspected source-role guard and materiality binding contradict those statements. Conversely, the [validator index](../../../tools/validators/domains/habitat/README.md) is an index, not proof that every listed profile, workflow, or consumer is operational.

Keep these three facts separate: **this config lane has no payload; bounded Habitat fixture validation exists elsewhere; proof/release/public operation is not established here.** The next config slice should identify one genuine consumer need, close its direct dependencies, add synthetic tests, and remain inactive where authority is unresolved. It need not rebuild the whole Habitat domain.

## Compatibility and parallel-authority guardrails

v0.4 recorded HabitatPatch, SuitabilityModel, ModelRunReceipt, shared-versus-domain trust-object, registry-topology, singular/plural triplet, and `biotopes` questions. Preserve those as verification debt, not as newly confirmed conflicts or blanket blockers on unrelated draft work.

For a selected consumer, inspect the current authoritative object, schema, alias register, and accepted decisions before binding. Do not choose by filename, case, modification time, or import accident. A compatibility path cannot be more permissive than its target; migration must preserve single-write authority, references, correction lineage, validation, and rollback. This revision moves or retires nothing.

## Logging, caches, tiles, indexes, exports, and derived-output invalidation

Diagnostics should use safe reason codes, stable references, versions and digests, not raw configuration, credentials, protected geometry, private endpoints, complete restricted descriptors/bundles, model inputs, sensitive prompts, hidden reasoning, or revealing stack traces.

A material config, source-role, model, rights, sensitivity, evidence, or release correction requires an affected-output inventory: caches, tiles/PMTiles/COGs, search/autocomplete, vector indexes, graph projections, reports/PDFs, downloads, screenshots/share links, alerts, Evidence Drawer/Focus payloads, AI retrieval/answer caches, and current-version aliases.

Stop unsafe selection/serving, record correction or withdrawal, invalidate affected derivatives, regenerate only from governed corrected inputs, and recheck evidence, policy, review and release. A Git revert alone does not prove stale or unsafe derivatives stopped being served.

## Failure behavior

These are required design dispositions, not a newly implemented config API or shared outcome enum.

| Condition | Required disposition |
|---|---|
| No selected payload or verified consumer | Remain unconfigured/inactive; do not infer activation. |
| Malformed input, duplicate/unknown keys, unsupported version, or precedence conflict | Reject atomically with safe diagnostics; no partial application. |
| Missing or conflicting authority, role mapping, object alias, or required profile | Hold consequential use; never choose a permissive fallback. |
| Model-to-observation/designation upgrade or habitat-to-occurrence inference | Deny the unsupported claim. |
| Unclear rights, sensitivity, geoprivacy, or reconstructable protected context | Hold, quarantine, restrict, or deny through the owning control. |
| Stale, partial, corrected, or withdrawn support | Preserve the state; abstain where a supported answer is unavailable. |
| Secret exposure or unsafe existing derivative | Stop affected use; invoke incident/correction handling and invalidate outputs. |
| Unknown affected outputs or unproved rollback | Hold the consequential transition. |

Validator `PASS`/failure, work-state `HOLD`, and runtime `ANSWER`/`ABSTAIN`/`DENY`/`ERROR` have distinct owners. None substitutes for source admission or release approval.

## Governed AI and generated language

AI may assist with bounded review and clearly labeled drafts; it cannot approve mappings, source rights, model fitness, sensitivity, review, or release. Scope and retrieve admissible evidence first; resolve `EvidenceRef -> EvidenceBundle`; apply policy, rights, sensitivity, review, and release checks; then cite with bounded confidence or abstain.

Maps, models, tiles, graphs, indexes, configs, and generated language are not root truth. Do not infer species presence/absence, invent evidence references, expose sensitive joins, or reuse corrected/withdrawn context because an answer sounds plausible.

## Migration and anti-bypass posture

When misplaced material is found, classify its responsibility and exposure before changing it. Stop unintended activation, route secrets or protected context to appropriate incident handling, and propose the smallest owning-root correction. Preserve old/new identity, affected consumers, hashes, lineage, tests, correction, and rollback; do not silently delete history or choose a parallel schema/policy/source home.

No migration, secret rotation, source-state change, policy amendment, or lifecycle action is executed by this README. Such remediation requires its own appropriate authority and handling.

## Rollback, correction, supersession, and invalidation

For this documentation-only revision, abandon the unintegrated branch or restore prior blob `010b05e30b1d9966cbfe00d87a1b72fcb9872a58` through a reviewed corrective change. Preserve concurrent edits; do not rewrite old receipts or unrelated files.

For a future consumed configuration: disable selection atomically, retain safe audit evidence, inventory affected outputs, quarantine/withdraw unsafe derivatives, restore a verified prior version or disabled state, correct governing records in their owning lanes, invalidate/regenerate outputs, and revalidate through release where applicable. Restoring text does not revoke exposed data or establish correction closure.

## Definition of done for the first payload

A reviewable **draft** identifies one consumer or explicitly proposed seam, justified placement, a dependency list, synthetic inputs, non-effects, tests, and a reversible plan. Unknown optional relationships may remain visible.

**Operational binding** additionally requires validated parser/schema/precedence, accepted applicable authority references, assigned accountable reviewers, no implicit activation, no secrets, anti-collapse and sensitive-join tests, deterministic failure behavior, and tested deactivation/invalidation/replay. Source admission and public release remain separate gates. Resolve only the aliases, mappings, rights, and profiles on that consumer's actual dependency path; do not infer approval from a green placeholder or held job.

## Open verification register

Existing IDs remain stable. Historical findings must be rechecked, not silently deleted or upgraded.

| ID | Remaining question / current disposition |
|---|---|
| `HAB-CFG-001` | CODEOWNERS route confirmed; accountable steward assignments and independent review remain unverified. |
| `HAB-CFG-002` | No executable config consumer found in the bounded path-reference search; external/dynamic consumers unknown. |
| `HAB-CFG-003` | Consumer-specific loading, discovery, precedence, and atomic reload remain unknown. |
| `HAB-CFG-004` | First payload format/schema is proposed; this README does not define a machine contract. |
| `HAB-CFG-005` | Verify accepted mapping for any Habitat/shared-role vocabulary crossing; NWI role remains unassigned here. |
| `HAB-CFG-006` | Recheck historical HabitatPatch contract aliases before binding. |
| `HAB-CFG-007` | Recheck historical SuitabilityModel path/case aliases before binding. |
| `HAB-CFG-008` | Recheck historical ModelRunReceipt placement question for the chosen consumer. |
| `HAB-CFG-009` | Verify shared authority and domain-profile use; do not duplicate trust-object semantics. |
| `HAB-CFG-010` | Recheck registry topology and stable canonical source record for the chosen dependency. |
| `HAB-CFG-011` | Verify any triplet consumer's accepted child path; config writes neither compatibility nor canonical data. |
| `HAB-CFG-012` | Recheck `biotopes` compatibility disposition; create no alternate authority. |
| `HAB-CFG-013` | Package exports/consumer wiring not audited in this pass; old scaffold observations are historical. |
| `HAB-CFG-014` | Inactive pipeline declarations do not prove executable processing or activation. |
| `HAB-CFG-015` | Verify exact relevant schema/profile enforcement; old permissive-schema findings are not a current whole-lane verdict. |
| `HAB-CFG-016` | Operational policy evaluation and its consumer binding remain unproved here. |
| `HAB-CFG-017` | Blanket-placeholder claim corrected: bounded role guard and materiality code/bindings exist; other indexed validators need their own evidence. |
| `HAB-CFG-018` | TODO-only claim corrected: substantive validation and explicit proof/release holds; exact-head hosted results remain separate. |
| `HAB-CFG-019` | Source rights, current terms, attribution, and allowed use need source-specific verification. |
| `HAB-CFG-020` | Model fitness, calibration, applicability, and threshold semantics need model-specific evidence. |
| `HAB-CFG-021` | Operational geoprivacy, transformation receipts, and reconstruction tests remain consumer-specific gates. |
| `HAB-CFG-022` | Prove affected-output discovery and cache/tile/index/export/AI invalidation for any operational consumer. |
| `HAB-CFG-023` | Release, correction, withdrawal, and rollback integration remain unproved by this config lane. |

## Safe language guide

Say **“no payload is tracked here”**, not “Habitat has no implementation.” Say **“the source-role fixture suite passed in a verified subset”**, not “Habitat is production-ready.” Say **“the workflow reports a proof/release hold”**, not “proof and publication checks passed.”

Say **“historical alias finding needs a current dependency check”**, not “all aliases are confirmed conflicted.” Say **“review route exists”**, not “independent approval occurred.” Describe designation, suitability, occurrence, source vintage, rights, uncertainty, and release state according to the evidence, not the map's appearance.

## Evidence ledger

Repository paths below are immutable-source locators when resolved at the evidence commit in metadata; relative links navigate the current branch and must be re-pinned for later claims.

| Evidence | Identity / bounded use |
|---|---|
| Prior target and direct directory listing | Target blob `010b05e30b1d9966cbfe00d87a1b72fcb9872a58`; `.gitkeep` blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. |
| Parent configuration README | Blob `c497e41466f3aaf934aeca4b9976a2fa8516ff21`; inherited non-secret/non-authority boundary. |
| Directory Rules and ADR-0029 | Adopted doctrine blob `fd49a0b83e55cef52c1124281f093e263526898d`; accepted adoption decision read directly. |
| CODEOWNERS | Blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61`; review routing only. |
| Habitat domain README | v1.4; landscape/species distinction and explicit NWI role uncertainty. Not a substitute for source admission. |
| Habitat validator index | Blob `96546505d1736aeefb6f26abff3d9a828fb81516`; mixed-maturity inventory, not an exhaustive audit. |
| Critical-habitat validator and tests | Blobs `0e1c859b493f9c485885a1e4ae66ff60bf376a6d` and `3fb512a9812affb8caec9750fc29cd749f82cddf`; reconstructed bytes matched; seven focused tests passed. |
| Critical-habitat workflow | Blob `704d911bd976acb65ba6beeadc5eb7df25660f73`; exact command and path-filter boundary. |
| Materiality adapter | Blob `931677daf9d4d54150cd10aadf8285c7ef8ae93e`; inspected entry binds its profile under `pipeline_specs/`, not this config directory. |
| Domain workflow | Blob `59771c027f688d7028a46c4635c0ec710b34e3ab`; materiality commands and explicit guarded proof/release holds. |
| Pipeline-spec README | Blob `fe4635bbcbe6a1101691836f89fc2672c76daa7b`; inactive declaration/profile index and validation navigation. |
| Bounded config-reference search | This README, parent, file-system plan, and historical generated-receipt references; no executable consumer surfaced. Search is not exhaustive absence proof. |

**Lineage consulted (not implementation evidence):** Drive `Directory Rules` (document ID `1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs`) and `kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf` (file ID `1Ys9Z_AYfEz6oStxY0YqZjih9DFHc5GA6`), plus Notion `KFM Hourly Habitat Domain Builder v1.0` (page ID `3caa9202-1bf6-8157-acf6-ef450096c987`). Their plans, old test claims, path proposals, and historical coordination do not override current GitHub evidence or accepted placement. Drive fixed-PDF byte identity was not independently audited in this pass.

**v0.5 change boundary:** preserves the document ID, prior H2 anchors, verification IDs, no-secrets/no-authority rules, explicit binding, role/model/occurrence distinctions, time/space/rights/sensitivity constraints, compatibility safeguards, and correction/invalidation/rollback obligations. Repetition is consolidated; old blanket maturity claims are replaced by bounded current evidence. No payload, code, schema, policy, source, workflow, lifecycle artifact, or release object changes.

## Status summary

**README-backed configuration boundary; mixed surrounding Habitat maturity; no operational configuration or publication authority established.** Author the next dependency-closed consumer slice reversibly, validate what it actually changes, and keep evidence, source admission, review, policy, release, and public exposure as separate decisions.

[Back to top](#top)
