<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-aquifer-observation
title: Aquifer Observation Contract — Hydrology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; PLACE; object-family-vs-link identity unresolved; schema missing; dedicated validation absent; no publication authority
owners:
  - "@bartytime4life — CODEOWNERS review route"
  - "Hydrology semantic steward assignment — NEEDS VERIFICATION"
  - "Geology/Hydrogeology seam steward assignment — NEEDS VERIFICATION"
created: 2026-06-22
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; hydrology; aquifer-observation; groundwater; cross-lane; private-property-risk; evidence-bound; release-gated; rollback-aware
related:
  - ./README.md
  - ./groundwater_well.md
  - ./water_level_observation.md
  - ./domain_observation.md
  - ./evidence_bundle.md
  - ../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../schemas/contracts/v1/domains/hydrology/README.md
  - ../../../tests/domains/hydrology/README.md
  - ../../../tools/validators/domains/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../release/candidates/hydrology/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../.github/workflows/hydrology-proof-slice.yml
  - ../../../.github/CODEOWNERS
tags: [kfm, contracts, hydrology, aquifer-observation, groundwater, observation, cross-lane-link, source-role, evidence-bundle, sensitivity, correction, rollback]
notes:
  - "Same-path semantic-contract modernization grounded in main@c980120a828eb0d8195cea706069db5ad68cbacf."
  - "Accepted Directory Rules v2 returns PLACE for this semantic Markdown under contracts/domains/hydrology/."
  - "The Hydrology glossary defines AquiferObservation as a groundwater-level or aquifer-state observation."
  - "The Hydrology object-family catalog separately treats AquiferObservation as a PROPOSED Geology seam/link object and leaves first-class-family versus link-record identity open."
  - "No paired AquiferObservation schema, dedicated fixture family, dedicated validator, or dedicated test was found at the pinned snapshot."
  - "Current executable Hydrology coverage is limited to EvidenceBundle alias shape/polarity plus process-level network denial; it does not validate this contract."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Aquifer Observation Contract — Hydrology

Semantic boundary for a proposed `AquiferObservation` that can associate a
groundwater-level or aquifer-state observation with aquifer context while
preserving source role, time, measurement basis, evidence, sensitivity, and
the Geology/Hydrogeology authority boundary.

> [!IMPORTANT]
> `AquiferObservation` has an unresolved repository identity. The Hydrology
> glossary defines it as an observation, while the object-family catalog treats
> it as a proposed cross-lane link record and leaves first-class family versus
> link record open. This contract preserves both facts. It does not settle that
> decision, create a machine shape, or authorize data admission or publication.

<!-- Keep adjacent GitHub alerts as separate blockquotes. -->

> [!WARNING]
> The expected paired schema is absent. No dedicated fixture, validator, or
> test for this object was found. Every field-shaped term in this document is
> semantic guidance until a separately reviewed schema and executable negative
> coverage exist.

## Quick navigation

- [Status and authority](#status-and-authority)
- [Placement and responsibility](#placement-and-responsibility)
- [Meaning and unresolved identity](#meaning-and-unresolved-identity)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Minimum semantic envelope](#minimum-semantic-envelope)
- [Source-role rules](#source-role-rules)
- [Measurement, time, and spatial rules](#measurement-time-and-spatial-rules)
- [Evidence, policy, and publication](#evidence-policy-and-publication)
- [Lifecycle posture](#lifecycle-posture)
- [Machine and validation posture](#machine-and-validation-posture)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Evidence ledger](#evidence-ledger)
- [Verification register](#verification-register)

## Status and authority

| Surface | Confirmed posture at the pinned snapshot | Consequence |
|---|---|---|
| Semantic contract | v0.2; `draft`; `PROPOSED` | Defines a reviewable semantic boundary only. |
| Canonical path | `contracts/domains/hydrology/aquifer_observation.md`; `PLACE` | Keep semantic edits here; do not create a flat or parallel contract. |
| Object identity | Glossary: groundwater-level or aquifer-state observation. Object catalog: proposed Geology seam/link object. | First-class object family versus link record remains open. |
| Expected schema | `schemas/contracts/v1/domains/hydrology/aquifer_observation.schema.json` is absent | No field, requiredness, enum, pattern, reference, or cross-field rule is machine-enforced for this object. |
| Dedicated fixtures and tests | No dedicated AquiferObservation family was found | No positive or negative object behavior is proven. |
| Hydrology validator coverage | Bounded EvidenceBundle alias shape/polarity and process-level network denial only | Does not validate AquiferObservation meaning, measurement, role, time, evidence closure, or public safety. |
| Hydrology policy | Domain policy README remains a `PROPOSED` greenfield scaffold | No accepted object-specific allow, deny, generalize, or review behavior is claimed here. |
| Proof and release | Hydrology proof workflow is an explicit hold; the candidate lane creates no release authority | No source, record, proof, release, deployment, or publication state is asserted. |

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes changes under `contracts/`
to `@bartytime4life`. That route is not a Hydrology stewardship assignment,
independent approval, policy decision, evidence review, release approval, or
proof that review occurred.

[Back to top](#top)

## Placement and responsibility

Accepted [Directory Rules v2](../../../docs/doctrine/directory-rules.md) and
[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
separate three authorities:

| Question | Owning root | This contract's relationship |
|---|---|---|
| What does the object or interface mean? | `contracts/` | This file owns the proposed AquiferObservation meaning. |
| What machine shape is valid? | `schemas/` | A future paired schema must own field shape and constraints. |
| Under what conditions is it allowed, denied, held, restricted, or abstained? | `policy/` | Policy must own exposure and decision rules. |

Path decision:

- Artifact kind: semantic Markdown contract.
- Authority owner: object meaning.
- Responsibility root: `contracts/`.
- Scope kind and ID: domain, `hydrology`.
- Existing canonical home: `contracts/domains/hydrology/`.
- Outcome: `PLACE`.
- Governing rules: `DIR-AUTHROOT-002` and `DIR-SCOPELANE-001` through
  `DIR-SCOPELANE-004`.

The same path may reference schema, policy, evidence, Geology, source,
validation, release, and runtime authorities. It must not absorb or duplicate
them.

[Back to top](#top)

## Meaning and unresolved identity

### Confirmed semantic core

The Hydrology glossary defines `AquiferObservation` as a
groundwater-level or aquifer-state observation and states that aquifer geometry
remains a Geology/Hydrogeology concern.

The narrow common meaning is:

> A time- and source-scoped groundwater observation associated with aquifer
> context by reference, without making the Hydrology record authoritative for
> aquifer geometry, stratigraphy, hydrogeologic interpretation, well ownership,
> water rights, or public-safe exposure.

### Unresolved type relationship

The current repository supports two proposed readings:

| Proposed reading | What it would mean | What remains unresolved |
|---|---|---|
| Observation profile | A groundwater measurement object carrying value, unit, measurement basis, time, qualifier, and evidence | Its relationship to `WaterLevelObservation`, required site/well linkage, identity slots, and schema shape |
| Cross-lane seam/link record | A record linking a Hydrology groundwater observation to Geology-owned aquifer context | Whether it carries measurement values or only typed references and seam metadata |

The object-family catalog explicitly leaves the first-class-family versus link
record question open. The Hydrology identity model lists core observation
families and `GroundwaterWell`, but does not define a dedicated
`AquiferObservation` identity row. Until that is resolved:

- do not assert a canonical JSON shape;
- do not invent a subtype or inheritance relationship;
- do not require a well link for every possible aquifer-state claim;
- do not treat the link as transferring authority between domains;
- do not use this contract as evidence that an implementation exists.

The safest present interpretation is a **proposed seam-aware observation
contract** whose stable machine identity still requires a separately reviewed
decision.

[Back to top](#top)

## Anti-collapse boundaries

| Do not collapse `AquiferObservation` into | Boundary |
|---|---|
| `GroundwaterWell` | A well/site identity and construction context is not a groundwater measurement. |
| `WaterLevelObservation` | The glossary currently frames WaterLevelObservation as gauge-height/stage. Any shared groundwater profile or subtype relationship must be explicit. |
| Geology/Hydrogeology aquifer identity | Hydrology may reference aquifer context; it does not own aquifer geometry, lithology, stratigraphy, or hydrogeologic interpretation. |
| Well registry or permit row | Administrative identity or authorization is not an observed aquifer-state value. |
| Water right, allocation, withdrawal, ownership, parcel, or title claim | Those claims retain their owning administrative or land authority and require separate evidence. |
| Modeled groundwater surface, interpolation, reconstruction, or forecast | Modeled output retains model identity, run lineage, uncertainty, and modeled role; it is never relabeled observed. |
| Aquifer, county, HUC, or regional aggregate | Aggregate scope and time window do not establish a well- or point-level reading. |
| No-data, below-detection, or missing reading | Absence is not numeric zero and must retain its source qualifier. |
| Retrieval, processing, release, or correction timestamp | KFM process time is not source observation time. |
| Public-safe geometry | Exact internal location and generalized, aggregate, withheld, or restricted public geometry are different representations with different authority. |
| AI summary or synthetic reconstruction | Generated language is interpretive and is not observation evidence or an admitted source. |
| Emergency or operational guidance | KFM Hydrology is not water-supply, drought-response, engineering, navigation, emergency, or life-safety authority. |

[Back to top](#top)

## Minimum semantic envelope

The following information categories are the minimum review target for a
future machine contract. They are not committed JSON field names, required
properties, enums, or accepted schema design.

| Category | Semantic obligation |
|---|---|
| Object identity | Distinguish the record from wells, gauge-stage observations, modeled surfaces, aggregates, and Geology identities. |
| Source identity | Resolve the source descriptor, source-native record or series identity, version/vintage, authority limits, rights, and attribution. |
| Claim-level source role | Preserve whether the supporting claim is observed, administrative, aggregate, modeled, regulatory, candidate, or synthetic. |
| Measurement | Preserve parameter/phenomenon, source value, normalized value where produced, unit, qualifier, no-data state, and provisional/final state. |
| Measurement basis | Preserve method, measuring point, datum/reference surface, vertical reference, precision, and conversion lineage when supplied. |
| Observation time | Record when the phenomenon was measured or observed. |
| Other temporal roles | Keep source, valid, retrieval, release, and correction times distinct where material. |
| Site or well context | Reference a `GroundwaterWell`, monitoring site, or other source location when the source and selected identity model require it. |
| Aquifer context | Reference a Geology/Hydrogeology-owned aquifer identity or context without copying or redefining its canonical geometry. |
| Spatial posture | Separate source location, exact internal location, generalized public location, aggregate public scope, withheld location, and restricted location. |
| Evidence | Resolve consequential claims through EvidenceRefs to admissible EvidenceBundles with claim scope and citations. |
| Sensitivity and policy | Record private-property, well-owner, infrastructure, resource-vulnerability, rights, and public-exposure decisions. |
| Validation | Identify the schema, validator revision, fixture class, report, and any skipped or held checks. |
| Correction and supersession | Preserve the prior identity, changed evidentiary content, reason, time, affected derivatives, and invalidation scope. |
| Release and rollback | Link the governed decision, public-safe carrier, release manifest, correction path, and rollback target when a public release exists. |

The Hydrology identity doctrine proposes a common identity shape based on source
identity, object role, temporal scope, and normalized digest. Field names,
normalization rules, digest inputs, and the identity consequences of a
measurement correction remain unimplemented for this object.

[Back to top](#top)

## Source-role rules

Source role is assigned per claim at admission and preserved through
transformation. The current source-role matrix does not include a dedicated
AquiferObservation object-family row, so this contract must not invent a
single default role for every possible record.

| Supporting role | Permitted interpretation | Forbidden interpretation |
|---|---|---|
| `observed` | May support a direct groundwater-level or aquifer-state measurement when source, time, value, unit, basis, qualifier, and evidence resolve | Does not establish aquifer geometry, ownership, rights, allocation, or regulation |
| `administrative` | May support well identity, permit, registry, or accounting context | Is not a measurement unless separate observed evidence supports the measurement claim |
| `aggregate` | May support a named aquifer, HUC, county, or time-window summary | Is not per-well, per-point, or instantaneous truth |
| `modeled` | May support a model-derived aquifer surface or estimate with model/run/uncertainty lineage | Is never an observed measurement |
| `regulatory` | May support a regulatory or administrative determination within its source authority | Does not become scientific observation merely because it references groundwater |
| `candidate` | May remain in WORK/QUARANTINE for validation and review | Has no public edge before governed promotion |
| `synthetic` | May be used as clearly labeled test or representation material | Is not an admitted Hydrology source or observed reality |

For a seam/link interpretation, each referenced endpoint keeps its own source
role and authority. The existence of the link does not upgrade either endpoint,
transfer Geology authority into Hydrology, or make a candidate public.

[Back to top](#top)

## Measurement, time, and spatial rules

### Measurement

- Preserve source value and unit before normalization.
- Record every unit conversion as a deterministic transform with original and
  resulting values, the conversion rule, and a receipt or validation record.
- Keep measuring point, datum/reference surface, and vertical reference
  explicit; values with incompatible or unknown bases must not be compared as
  if aligned.
- Preserve provisional/final, estimated, censored, no-data, below-detection,
  corrected, and source quality flags.
- A difference or trend is a derived claim. It requires the identities and
  compatible bases of every contributing observation.

### Time

| Temporal role | Meaning |
|---|---|
| Observation time | When the source says the groundwater phenomenon was measured |
| Source time | Source version, publication, update, or assertion time |
| Valid time | Interval during which a source claim applies, when supplied |
| Retrieval time | When KFM obtained the bytes; never observation truth |
| Release time | When a governed KFM release became effective; not source time |
| Correction time | When correction or supersession lineage was recorded |

Missing or ambiguous observation time narrows the supported claim. It must not
be silently replaced with retrieval, file-modification, ingestion, or release
time.

### Spatial posture

An observation may require precise internal location to preserve measurement
meaning, but public precision is a separate decision. Private-well,
owner/parcel, protected-infrastructure, resource-vulnerability, and
reverse-engineerable joins require policy review and may require
generalization, aggregation, redaction, delayed access, or denial.

Aquifer context is always a reference to the owning Geology/Hydrogeology
authority. A public map symbol, generalized footprint, or derived surface must
not become the canonical aquifer identity or the original observation
location.

[Back to top](#top)

## Evidence, policy, and publication

Schema validity, when a schema exists, will establish shape only. A public or
semi-public AquiferObservation claim additionally requires support appropriate
to the claim:

1. admitted source identity, role, version, rights, and permitted claims;
2. stable object identity and observation time;
3. measurement value, unit, basis, method, and qualifier;
4. resolvable EvidenceRef-to-EvidenceBundle support;
5. cross-lane aquifer context without authority transfer;
6. sensitivity and public-safe spatial treatment;
7. applicable policy outcome and required review;
8. correction and supersession path;
9. governed release decision, manifest, carrier, and rollback target.

Current executable Hydrology tests validate only the shared EvidenceBundle
alias shape, one valid/invalid fixture pair, and process-level network denial.
They do not resolve evidence, evaluate this object, apply Hydrology policy,
construct proof, close a catalog, approve release, or publish data.

| Condition | Finite public-surface posture |
|---|---|
| Evidence-backed, role-preserved, policy-allowed, public-safe, released claim | `ANSWER` may be considered by the governed runtime |
| Missing or ambiguous identity, role, time, unit, basis, evidence, or release support | `ABSTAIN` or retain the record in `HOLD` |
| Forbidden role collapse, sensitive exposure, trust-membrane bypass, or life-safety framing | `DENY` |
| Schema, resolver, validator, policy, or runtime failure | `ERROR`; never fall back to raw or uncited output |

`ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are runtime-envelope outcomes.
`HOLD`, `PASS`, and `FAIL` belong to review or validation gates and must not be
collapsed into runtime answers.

[Back to top](#top)

## Lifecycle posture

| Phase | AquiferObservation obligation |
|---|---|
| RAW | Preserve source bytes or stable locator, source-native identity, source role, times, values, units, basis, qualifiers, rights, and sensitivity metadata. |
| WORK / QUARANTINE | Resolve the proposed object/link interpretation; normalize without overwriting source values; hold role, time, unit, datum, rights, identity, or sensitive-join gaps. |
| PROCESSED | Emit a validated candidate only under an accepted shape, with deterministic identity, transform lineage, and explicit unresolved findings. |
| CATALOG / TRIPLET | Reference the candidate and evidence by stable identity; graph or catalog projections do not become observation truth. |
| RELEASE CANDIDATE | Assemble public-safe carrier, evidence, policy, review, validation, correction, and rollback support; candidate placement itself grants no release authority. |
| PUBLISHED | Serve only through governed interfaces and release-approved carriers. Public clients do not read RAW, WORK, QUARANTINE, restricted, or unreleased state. |
| CORRECTED / SUPERSEDED | Preserve lineage, invalidate affected derivatives and caches, and issue the appropriate correction or withdrawal record. |

Promotion is a governed state transition, not a file move.

[Back to top](#top)

## Machine and validation posture

### Confirmed implementation boundary

| Surface | Current state | What it does not establish |
|---|---|---|
| Expected AquiferObservation schema | Missing at the canonical paired path | No object shape or required fields |
| `groundwater_well.schema.json` | `PROPOSED`; empty `properties`; `additionalProperties: true` | Does not validate AquiferObservation or meaningful GroundwaterWell semantics |
| Hydrology schema README | Stale draft inventory that says concrete schemas were not confirmed | Must not override current file-by-file repository evidence |
| Hydrology contract README | v0.3 inventory records AquiferObservation among five contract-declared missing schemas | Does not create the missing schema |
| Dedicated AquiferObservation fixture family | Not found | No valid, invalid, correction, or sensitive-location examples |
| Dedicated AquiferObservation validator | Not found | No source-role, measurement, time, seam, or policy enforcement |
| Dedicated AquiferObservation test | Not found | No object-specific executable behavior |
| `test_hydrology_smoke.py` | Three executable tests for EvidenceBundle alias shape/polarity and network denial | Not this object, evidence closure, policy, proof, release, or publication |
| `domain-hydrology` workflow | Runs bounded Hydrology readiness and shape checks with explicit broader holds | No real Hydrology truth or publication authority |
| `hydrology-proof-slice` workflow | Explicit readiness hold; no accepted proof producer or closure command | No proof, catalog closure, promotion, release, or publication |

### Required implementation sequence

1. Resolve first-class object family versus cross-lane link record through the
   owning semantic and seam review.
2. Define the relationship to `GroundwaterWell`,
   `WaterLevelObservation`, the shared observation envelope, and
   Geology/Hydrogeology aquifer identity.
3. Specify deterministic identity and correction behavior.
4. Add the canonical schema under `schemas/`; do not embed a second schema
   inside this contract.
5. Add synthetic valid, invalid, correction, aggregate, modeled,
   administrative, missing-basis, and sensitive-location fixtures.
6. Add a dedicated fail-closed validator and deterministic no-network tests.
7. Implement and test source-role, evidence, rights, sensitivity,
   public-geometry, release, correction, and rollback policy.
8. Wire bounded CI without treating a green check as source admission,
   evidence closure, or publication.

[Back to top](#top)

## Compatibility, correction, and rollback

The following future changes are compatibility-significant and require an
explicit version, migration, and consumer review:

- resolving observation-profile versus link-record identity;
- changing the relation to `GroundwaterWell` or `WaterLevelObservation`;
- changing deterministic identity or digest inputs;
- changing required measurement, unit, datum, method, qualifier, or time
  semantics;
- changing permitted source-role bases;
- changing aquifer-reference ownership or cross-lane seam behavior;
- changing exact/internal versus public/generalized spatial treatment;
- changing correction, supersession, release, or rollback relationships.

Corrections must preserve prior identity and downstream reliance. A source
correction to value, unit, datum, time, well/site link, aquifer context, or
location treatment must identify affected records, evidence, derivatives,
catalog/graph projections, releases, caches, and public responses.

Rollback this documentation change if it:

- resolves the open type identity without governing review;
- presents proposed fields as an implemented schema;
- implies that current Hydrology smoke tests validate this object;
- transfers aquifer geometry authority into Hydrology;
- collapses administrative, aggregate, modeled, candidate, or synthetic
  material into observed truth;
- weakens private-well or sensitive-location controls;
- implies source admission, proof, release, or publication.

Before merge, close the draft pull request and abandon the scoped branch. After
an independently authorized merge, use a focused revert or corrective pull
request against the actual merge commit. Reverting this Markdown file does not
undo an external observation, source correction, policy decision, release, or
publication.

[Back to top](#top)

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| [`contracts/domains/hydrology/README.md`](./README.md) | CONFIRMED at pinned snapshot | Canonical path, 23-contract inventory, five missing contract-declared schemas, bounded validation posture | Directory index only; does not upgrade this contract |
| [`GLOSSARY.md`](../../../docs/domains/hydrology/GLOSSARY.md) | CONFIRMED | Defines AquiferObservation as groundwater-level or aquifer-state observation and preserves the Geology geometry boundary | Does not define machine shape or identity |
| [`OBJECT_FAMILIES.md`](../../../docs/domains/hydrology/OBJECT_FAMILIES.md) | CONFIRMED draft doctrine | Treats AquiferObservation as a proposed Geology seam/link object and records the first-class-versus-link question | Does not resolve the open question |
| [`SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md) | CONFIRMED doctrine; PROPOSED implementation | Defines seven source roles and groundwater family role possibilities | Has no dedicated AquiferObservation object-family row; enforcement remains proposed |
| [`IDENTITY_MODEL.md`](../../../docs/domains/hydrology/IDENTITY_MODEL.md) | CONFIRMED doctrine; PROPOSED field realization | Common source/object-role/time/digest identity shape and six distinct temporal roles | Does not define a dedicated AquiferObservation identity row |
| [`BOUNDARY.md`](../../../docs/domains/hydrology/BOUNDARY.md) | CONFIRMED draft doctrine | Hydrology/Geology boundary and private-well/public-safety constraints | Does not implement policy or public-safe transforms |
| Expected paired schema fetch | CONFIRMED missing | No file exists at `schemas/contracts/v1/domains/hydrology/aquifer_observation.schema.json` | Does not prove no alternative experimental shape exists elsewhere |
| [`groundwater_well.schema.json`](../../../schemas/contracts/v1/domains/hydrology/groundwater_well.schema.json) | CONFIRMED scaffold | Related schema exists with empty properties and open additional properties | Not an AquiferObservation schema |
| [`test_hydrology_smoke.py`](../../../tests/domains/hydrology/test_hydrology_smoke.py) | CONFIRMED bounded executable slice | Three tests cover EvidenceBundle alias shape/polarity and process-level network denial | No AquiferObservation behavior |
| [Hydrology validator README](../../../tools/validators/domains/hydrology/README.md) | CONFIRMED current index | Groundwater/aquifer validation is a proposed future child lane | No dedicated validator exists |
| [Hydrology policy README](../../../policy/domains/hydrology/README.md) | CONFIRMED scaffold | Policy has a canonical responsibility root | No accepted object-specific policy behavior |
| [`domain-hydrology.yml`](../../../.github/workflows/domain-hydrology.yml) | CONFIRMED bounded CI | Executes readiness and EvidenceBundle alias checks and guards broader holds | No source truth, policy, proof, or release closure |
| [`hydrology-proof-slice.yml`](../../../.github/workflows/hydrology-proof-slice.yml) | CONFIRMED explicit hold | Detects readiness drift without running a proof producer | No proof or publication |
| Accepted [Directory Rules v2](../../../docs/doctrine/directory-rules.md) through [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | CONFIRMED adopted placement authority | `contracts/` owns meaning; Hydrology is a sparse domain lane; parallel authority is denied | Placement does not grant truth, policy, release, or publication |

[Back to top](#top)

## Verification register

| ID | Status | Required closure |
|---|---|---|
| `HYD-AQOBS-01` | `OPEN` | Decide whether AquiferObservation is a first-class observation family, a profile of another observation, a cross-lane link record, or a split of those responsibilities. |
| `HYD-AQOBS-02` | `NEEDS VERIFICATION` | Define its exact relationship to GroundwaterWell, WaterLevelObservation, DomainObservation, and Geology/Hydrogeology aquifer identity. |
| `HYD-AQOBS-03` | `NEEDS VERIFICATION` | Define deterministic identity, normalization, digest, versioning, and correction rotation rules. |
| `HYD-AQOBS-04` | `MISSING` | Add the paired schema only after the semantic identity decision. |
| `HYD-AQOBS-05` | `MISSING` | Add public-safe synthetic positive, negative, correction, and sensitive-join fixtures. |
| `HYD-AQOBS-06` | `MISSING` | Add dedicated validator and deterministic no-network tests for role, measurement, unit, datum, time, seam, evidence, and public-safe behavior. |
| `HYD-AQOBS-07` | `NEEDS VERIFICATION` | Define source admission and rights posture for each intended groundwater source family. |
| `HYD-AQOBS-08` | `NEEDS VERIFICATION` | Implement policy for private wells, owner/parcel inference, protected infrastructure, vulnerable resources, and exact public geometry. |
| `HYD-AQOBS-09` | `HELD` | Prove EvidenceRef-to-EvidenceBundle closure, catalog/proof agreement, release, correction, and rollback before any public edge. |

Re-review this contract when its identity decision, paired schema, fixtures,
validator, tests, source registry, policy, Geology seam, evidence closure,
release posture, public consumer, correction behavior, or rollback support
changes.

[Back to top](#top)
