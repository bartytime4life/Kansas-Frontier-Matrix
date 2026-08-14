<a id="adr-xxxx-atmosphere-knowledge-character-vocabulary"></a>

# ADR-XXXX: Use a Closed Atmosphere Knowledge-Character Vocabulary

KFM should use one closed, versioned Atmosphere/Air `knowledge_character` vocabulary to state the epistemic kind of every governed Atmosphere domain object, preserve that character through evidence and release flows, and fail closed when a record is missing, unknown, contradictory, or presented as a different kind of knowledge.

> [!CAUTION]
> This is an **unassigned proposed ADR candidate**, not an accepted decision. `ADR-XXXX` is a placeholder, and the canonical ADR index classifies this file as `not-assigned`. The repository's bounded six-character fixture validator is implementation evidence for selected anti-collapse rules; it does **not** accept this ADR, establish the complete vocabulary, activate policy, resolve evidence, or authorize release or publication.

**Quick links:** [Status](#status) · [Evidence boundary](#evidence-boundary) · [Context](#context) · [Decision](#decision) · [Vocabulary](#closed-vocabulary) · [Enforcement](#enforcement-contract) · [Current maturity](#current-implementation-maturity) · [Options](#options-considered) · [Consequences](#consequences) · [Convergence](#implementation-and-convergence) · [Acceptance](#validation-and-acceptance-gates) · [Rollback](#rollback-correction-and-supersession) · [Open questions](#open-questions) · [References](#evidence-and-references)

---

## Status

| Field | Value |
| --- | --- |
| **ID** | `ADR-XXXX` — unassigned placeholder |
| **Decision status** | `proposed` / `not-assigned` |
| **Date** | 2026-08-14 |
| **Deciders** | NEEDS VERIFICATION |
| **Affected stewards** | Atmosphere domain, architecture, source, evidence, contracts, schemas, policy, sensitivity, validation, governed API, UI/AI, release, correction, and rollback — assignments NEED VERIFICATION |
| **Supersedes** | None verified |
| **Superseded by** | None |
| **Directory Rules classification** | Non-structural, cross-component vocabulary and anti-collapse decision; the human decision record belongs in `docs/adr/` |
| **Primary responsibility root** | `docs/` |
| **Path migration** | No; this candidate remains at its tracked scaffold path until a reviewed numbering decision |
| **Implementation effect of this revision** | Documentation only |
| **Release or publication effect** | None |
| **Truth posture** | CONFIRMED repository evidence / PROPOSED decision / PARTIAL bounded implementation / UNKNOWN end-to-end enforcement |

The tracked path is `docs/adr/ADR-XXXX-atmosphere-knowledge-character-vocabulary.md`. Modernizing this existing scaffold in place preserves its inventory identity and does not reserve an ADR number, accept the decision, or create a parallel authority surface.

---

## Evidence boundary

This revision is grounded in repository evidence at:

```text
repository: bartytime4life/Kansas-Frontier-Matrix
base ref:   main
base SHA:   3e1a929a5e23f570b40c56e473b08ef65c3c5673
prior blob: c101657be0915331693ea1bd8a44a03801bdfbb4
```

### Truth labels used here

| Label | Meaning in this ADR |
| --- | --- |
| **CONFIRMED** | Verified from current repository bytes, an exact hosted workflow result, or the accepted Directory Rules decision |
| **PROPOSED** | The decision, token semantics, required behavior, or future convergence step is not accepted or fully implemented |
| **NEEDS VERIFICATION** | A concrete owner, mapping, consumer, policy binding, registry placement, or review remains to be checked |
| **UNKNOWN** | The inspected surfaces do not support a stronger conclusion |
| **CONFLICTED** | Current surfaces make incompatible authority, naming, or maturity claims |
| **HELD** | Graduation or release is intentionally blocked while prerequisites remain open |

### Current repository evidence

| Surface | CONFIRMED observation at the evidence checkpoint | Limit |
| --- | --- | --- |
| This file | The tracked target was a five-line `PROPOSED scaffold` sourced from `MISSING_OR_PLANNED_FILES.md`. | A planned path and scaffold do not establish a decision. |
| [`docs/adr/INDEX.md`](./INDEX.md) | Lists this exact path as an explicit `ADR-XXXX` placeholder with decision status `not-assigned`. | Index presence does not reserve a number or accept a decision. |
| [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) and [`directory-rules.md`](../doctrine/directory-rules.md) | ADR-0029 accepts the exact Directory Rules v2 bytes and confirms `docs/adr/` as the human ADR authority. | Placement authority does not decide this vocabulary or prove implementation. |
| [`KNOWLEDGE_CHARACTERS.md`](../domains/atmosphere/KNOWLEDGE_CHARACTERS.md) | Defines the Atmosphere concept, the eleven candidate machine-style values, source-role separation, immutability, and anti-collapse rationale. | It is a draft human-facing standard and cannot independently accept the enum. |
| [`KNOWLEDGE_CHARACTER_REGISTRY.md`](../domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md) | Acts as a thin index and records the enum and machine-registry home as open. | Some maturity statements predate the bounded validator and are stale planning evidence. |
| [`contracts/domains/atmosphere/knowledge_character.md`](../../contracts/domains/atmosphere/knowledge_character.md) | Defines draft semantic meaning, invariants, exclusions, and recommended fields. | It is draft; the paired schema and machine registry remain incomplete. |
| [`contracts/cross_domain/knowledge_character.md`](../../contracts/cross_domain/knowledge_character.md) | Records a broader anti-collapse pattern for cross-domain consumers. | It does not make the Atmosphere token set a global KFM enum. |
| [`knowledge_character.schema.json`](../../schemas/contracts/v1/domains/atmosphere/knowledge_character.schema.json) | Exists as a `PROPOSED` JSON Schema scaffold with empty `properties` and `additionalProperties: true`. | It enforces neither a closed vocabulary nor the anti-collapse rules. |
| [`data/registry/sources/atmosphere/knowledge_character.json`](../../data/registry/sources/atmosphere/knowledge_character.json) | Exists as a placeholder generated from a path inventory. | It is not a complete machine registry and its source-registry placement does not make it vocabulary authority. |
| [`validate_knowledge_character.py`](../../tools/validators/domains/atmosphere/validate_knowledge_character.py) | Implements a deterministic, no-network, six-character synthetic fixture profile with bounded inputs and exact findings. | It explicitly does not define the canonical enum, evaluate Rego, resolve evidence, admit sources, assess air quality, issue alerts, or authorize promotion/release/publication. |
| [`test_knowledge_character_registry.py`](../../tests/domains/atmosphere/test_knowledge_character_registry.py) | Contains 14 focused test methods covering six valid fixtures, five exact invalid fixtures, missing/unknown/multiple states, closed shapes, limits, deterministic output, non-echoing errors, and network denial. | These are fixture-contract tests, not live-domain or release proof. |
| [`fixtures/domains/atmosphere/knowledge_character/`](../../fixtures/domains/atmosphere/knowledge_character/) | Contains six synthetic valid cases and five synthetic fail-closed cases, all generalized and free of live source payloads or exact station coordinates. | Five proposed vocabulary values have no positive fixture in this profile. |
| [`policy/domains/atmosphere/README.md`](../../policy/domains/atmosphere/README.md) | Records thirteen default-only proposed Rego scaffolds, no accepted entrypoint, no active bundle, and no verified evaluator or production consumer. | Policy intent is not active enforcement. |
| [`domain-atmosphere.yml`](../../.github/workflows/domain-atmosphere.yml) | Runs the bounded knowledge-character fixture tests and positive/negative validator calls with no-network controls. The exact-main run `31825311905` at this SHA completed successfully. | A green bounded workflow does not accept the vocabulary or establish evidence, policy, proof, release, deployment, or publication. |
| [`genrec-atmosphere-knowledge-character-fixture-validator-20260802.json`](../../data/receipts/generated/genrec-atmosphere-knowledge-character-fixture-validator-20260802.json) | Records the bounded implementation artifact set and hashes. | A generated receipt records work; it is not human review, proof of truth, policy approval, or release authority. |

### Evidence interpretation

The repository already contains a meaningful **bounded proof** of selected anti-collapse behavior. It does not yet contain one accepted, closed, end-to-end vocabulary authority. This ADR must therefore distinguish:

1. **The proposed decision** — the full Atmosphere vocabulary and semantic rules.
2. **The current bounded implementation** — six synthetic character pairings and selected negative cases.
3. **Implementation graduation** — schema, registry, policy, all-token fixtures, consumers, evidence closure, correction, and rollback.
4. **Governed release** — a later state transition that this ADR cannot perform.

---

## Context

Atmosphere data is unusually vulnerable to epistemic and authority collapse. The following products can look similar in a table, map, popup, API response, or AI summary while representing materially different kinds of knowledge:

- a direct instrument concentration;
- a public AQI report;
- a certified or historical regulatory archive;
- a low-cost sensor value;
- a forecast or reanalysis model field;
- a satellite retrieval or mask;
- a baseline-relative climate anomaly;
- a multi-source fusion product;
- supporting meteorology;
- an official advisory reference;
- station or network metadata.

Without a closed character vocabulary, a downstream consumer can silently present:

- modeled values as observations;
- AQI categories or index values as pollutant concentrations;
- aerosol optical depth as ground-level PM2.5;
- a historical or certified archive as a current condition;
- low-cost sensor output as regulatory-grade evidence;
- a fusion product as a direct measurement;
- climate context as a local event observation;
- advisory metadata as KFM-issued life-safety guidance;
- network or station metadata as a measured atmospheric value;
- precise site coordinates on a public surface without policy review.

These are not cosmetic labeling errors. They change what a claim means, which evidence can support it, which policy applies, what time semantics are required, and whether the claim can safely reach a public client.

### Decision drivers

- **Inspectable claims** — a user must be able to tell what epistemic kind supports a claim.
- **Cite or abstain** — missing or unresolved character state cannot be guessed.
- **Source-role integrity** — source authority and object epistemic character are related but distinct.
- **Temporal integrity** — observed, issued, valid, forecast, archive, retrieval, baseline, release, and correction time cannot collapse.
- **Deterministic identity** — material re-characterization must not silently mutate an existing governed object.
- **Policy-aware release** — low-cost sensors, advisory context, exact sites, and derivative products carry different obligations.
- **Cross-domain safety** — Hazards, Agriculture, Hydrology, Habitat, and public Focus Mode consumers must preserve the Atmosphere object's character.
- **Finite validation** — schemas, validators, policy, APIs, UI, and AI need stable values and reasoned failure outcomes.
- **Reversibility** — incorrect characterization must support correction, supersession, cache invalidation, and rollback.
- **No parallel authority** — ADR, docs, contracts, schema, registry, policy, fixtures, and release records must have distinct responsibilities.

### Scope

This decision applies to governed Atmosphere/Air domain objects that can participate in evidence, claims, joins, catalog records, release candidates, governed API responses, MapLibre layers, Evidence Drawer payloads, exports, or AI interpretation.

It governs:

- the exact Atmosphere token set;
- the semantic meaning and minimum guards of each token;
- the rule that each governed Atmosphere domain object carries exactly one character;
- source-role separation;
- immutability and re-characterization;
- anti-collapse outcomes;
- the responsibility split among docs, contracts, schemas, registry projection, policy, validators, consumers, and release controls;
- graduation from the current bounded fixture profile.

### Out of scope

This ADR does not:

- define or replace the canonical cross-domain `source_role` vocabulary;
- make the Atmosphere tokens a global enum for every KFM domain;
- choose a new root or create a parallel schema, registry, policy, evidence, proof, receipt, or release home;
- settle the machine-registry path when placement authority remains unresolved;
- select scientific correction models, calibration equations, air-quality thresholds, health guidance, or regulatory methods;
- determine whether a specific source, sensor, product, model, archive, or advisory is admissible;
- activate the current Rego scaffolds or choose a policy runtime entrypoint;
- resolve a live `EvidenceRef` to an `EvidenceBundle`;
- authorize source activation, live ingestion, alerting, release, deployment, or publication;
- replace object-family contracts, source descriptors, policy decisions, review records, release manifests, correction notices, or rollback cards.

---

## Decision

> [!IMPORTANT]
> **PROPOSED decision:** KFM Atmosphere/Air will use the exact field name `knowledge_character` with a closed, versioned set of eleven uppercase snake-case token values. Every governed Atmosphere domain object carries exactly one token. The umbrella phrase **“knowledge character” is the concept and field name, not a twelfth enum value**.

The proposed token set is:

```text
OBSERVED_SENSOR
PUBLIC_AQI_REPORT
REGULATORY_ARCHIVE
LOW_COST_SENSOR
ATMOSPHERIC_MODEL_FIELD
REMOTE_SENSING_MASK
CLIMATE_ANOMALY_CONTEXT
DERIVED_FUSION
METEOROLOGICAL_CONTEXT
ALERT_AND_ADVISORY_CONTEXT
NETWORK_AND_SITE_CONTEXT
```

No unregistered free text, inferred synonym, source name, object-family name, or UI label may substitute for these tokens in a governed machine payload.

### Core semantic rules

1. **Exactly one.** A governed Atmosphere domain object must carry exactly one `knowledge_character`.
2. **Closed vocabulary.** Unknown tokens, aliases, multiple tokens, or missing values fail closed.
3. **Distinct from source role.** `source_role` states the authority kind of the source; `knowledge_character` states the epistemic kind of the normalized Atmosphere object. Neither replaces the other.
4. **Assigned before governed identity closes.** A candidate receives its character during normalization/admission review before deterministic processed identity and release lineage are finalized.
5. **Immutable after identity.** Once a governed object identity is minted, the character cannot be edited in place. A material re-characterization creates a replacement identity and correction/supersession lineage.
6. **Evidence-bound.** Character state must be supportable from the source descriptor, method/product metadata, transformation lineage, and evidence references appropriate to the claim.
7. **Time-bound.** Each character requires the time kinds necessary to prevent live, historical, forecast, archive, retrieval, baseline, and release states from being confused.
8. **Policy-aware.** Character state may trigger caveats, generalization, review, restrictions, abstention, denial, or a release hold. It is not itself a `PolicyDecision`.
9. **Release-neutral.** A recognized token, valid schema, passing validator, or green workflow does not grant release or publication.
10. **Preserved through derivatives and joins.** Consumers must retain the original character; a derived product must also declare its own character and preserve per-input lineage.
11. **Visible at consequential surfaces.** Governed API, Evidence Drawer, exports, and AI responses must expose the character or a public-safe equivalent when it materially affects interpretation.
12. **Correctable and reversible.** Character corrections must propagate through indexes, catalog/triplet projections, derived artifacts, caches, public surfaces, and rollback targets.

---

## Closed vocabulary

The definitions below are proposed normative semantics for eventual acceptance. They do not claim that the present schema, registry, policy, or all consumers enforce them.

| Token | Normative meaning | Minimum required guards | Must not be presented as |
| --- | --- | --- | --- |
| `OBSERVED_SENSOR` | A direct atmospheric measurement from an instrument at a station, platform, or governed observation location. | Instrument/method identity, unit, observation time, QA/calibration status, source descriptor, evidence support, spatial-sensitivity posture. | A model field, AQI report, regulatory determination, advisory, or unqualified low-cost value. |
| `PUBLIC_AQI_REPORT` | An authority-published air-quality index or category report. | Issuing authority, report/product identity, pollutant basis, issue/valid/freshness times, source reference, evidence and release state. | Raw pollutant concentration, KFM regulatory determination, or health/life-safety instruction. |
| `REGULATORY_ARCHIVE` | A regulatory or certified historical record, archive, determination, or revised/certified dataset. | Authority, archive/certification status, vintage, revision lineage, applicable period, retrieval time, supersession/correction status. | A live observation merely because it is authoritative or recently retrieved. |
| `LOW_COST_SENSOR` | A reading from a low-cost, community, consumer, or non-reference-grade sensor class that needs explicit qualification. | Device/network identity, method class, correction/calibration profile where used, confidence/limitations, collocation or evaluation context where claimed, drift/transferability caveats, public-use review. | Regulatory-grade truth, reference-equivalent concentration, or uncaveated public evidence. |
| `ATMOSPHERIC_MODEL_FIELD` | A forecast, hindcast, reanalysis, numerical weather, chemical-transport, dispersion, or other modeled atmospheric field. | Model and version, run/reference/valid times, parameter/unit, grid/vertical support, initialization/forcing lineage, uncertainty or ensemble context, limitations. | An observation or direct instrument measurement. |
| `REMOTE_SENSING_MASK` | A satellite, airborne, or other remotely sensed retrieval, raster, mask, classification, or proxy. | Platform/sensor/product identity, algorithm and version, acquisition/retrieval times, spatial resolution, quality flags, cloud/missing-data posture, uncertainty/limitations. | Ground-level concentration, confirmed impact, or direct station observation. |
| `CLIMATE_ANOMALY_CONTEXT` | A baseline-relative climate normal, anomaly, percentile, or climatological context product. | Baseline/reference period, dataset and method, aggregation geography/time, update/revision state, uncertainty and limitations. | A current local event, station observation, forecast, or source-native advisory. |
| `DERIVED_FUSION` | A value, surface, classification, or narrative derived from more than one input or from a transformation that combines epistemically distinct inputs. | Complete per-input lineage, per-input knowledge characters, transformation/spec identity, output uncertainty, temporal/spatial compatibility checks, release caveat. | A direct observation, single-source regulatory record, or source-native product. |
| `METEOROLOGICAL_CONTEXT` | Supporting meteorological observation or modeled context used to interpret an Atmosphere claim, such as wind, mixing height, humidity, or boundary-layer state. | Parameter/unit, source and source role, observed-or-modeled distinction, relevant times, method, evidence and limitations. | The pollutant observation, impact determination, or life-safety instruction it helps interpret. |
| `ALERT_AND_ADVISORY_CONTEXT` | A governed reference to an external authority's alert, advisory, bulletin, watch, warning, or related status, carried for context and referral. | Issuer, verified official source, product identity, issue/effective/expiry/cancel/supersession times, freshness, status, non-emergency disclosure, correction lineage. | A KFM-issued alert, paraphrased protective-action guidance, or substitute for the official life-safety authority. |
| `NETWORK_AND_SITE_CONTEXT` | Station, network, operator, equipment, siting, or site metadata used to interpret other Atmosphere objects. | Operator/program, site/network identity, metadata version/effective interval, public-safe geometry, sensitivity and generalization review, lineage. | An atmospheric measurement, modeled field, or permission to expose exact site coordinates. |

### Vocabulary versioning

The accepted implementation must give the vocabulary its own explicit version or immutable registry digest. Adding, removing, renaming, merging, or materially redefining a token is a compatibility-significant change and requires:

- a successor or amendment decision;
- schema and registry versioning;
- compatibility fixtures and migration mapping;
- consumer impact analysis;
- correction and rollback planning;
- no silent rewrite of previously released objects.

Display labels may be localized or made reader-friendly, but the governed token and its meaning must remain stable and traceable.

---

## Enforcement contract

The vocabulary is only useful when each responsibility root performs its own part without absorbing another root's authority.

### Responsibility split

| Responsibility | Owning surface | Required behavior after acceptance |
| --- | --- | --- |
| Architectural choice and rationale | This ADR in `docs/adr/` | Record the exact token set, semantics, alternatives, consequences, and supersession history. |
| Human domain explanation | `docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md` | Explain the vocabulary, examples, anti-collapse behavior, and consumer guidance without claiming machine enforcement. |
| Human registry index | `docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md` | Remain a thin index or generated projection; do not become a second hand-maintained semantic authority. |
| Semantic object meaning | `contracts/domains/atmosphere/knowledge_character.md` | Define the implementable contract and reference this ADR. |
| Cross-domain pattern | `contracts/cross_domain/knowledge_character.md` | Preserve the general anti-collapse concept without making Atmosphere tokens globally canonical. |
| Machine-checkable shape | `schemas/contracts/v1/domains/atmosphere/` | Enforce exactly one supported token and the accepted version/reference fields; remain separate from policy and registry data. |
| Machine vocabulary projection | ADR-selected canonical registry/control-plane home | Store the versioned token set and metadata. The existing source-registry placeholder is not promoted by this decision. |
| Source identity and source role | Governed `SourceDescriptor` surfaces | Establish source authority, method/product identity, rights, cadence, and source role independently. |
| Admissibility and obligations | `policy/domains/atmosphere/` plus accepted shared policy | Return finite policy decisions and obligations; do not infer evidence or release from the token alone. |
| Deterministic validation | `tools/validators/`, `fixtures/`, and `tests/` | Validate closed values, required guards, forbidden collapses, bounded input, safe errors, and compatibility. |
| Evidence support | `EvidenceRef` / `EvidenceBundle` owning surfaces | Support the claim and character assignment; a character label never substitutes for evidence. |
| Public delivery | Governed API and released artifacts | Carry character, evidence, time, policy, review, release, and correction state appropriate to the consumer. |
| UI and AI interpretation | MapLibre shell, Evidence Drawer, export, Focus Mode | Present clear distinctions and finite outcomes; never hide a collapse behind styling or fluent text. |
| Release, correction, withdrawal, rollback | `release/` and owning accountability families | Gate public exposure, preserve lineage, invalidate stale derivatives, and support reversal. |

### Source role and knowledge character

The two axes answer different questions:

| Axis | Question | Assignment point | Mutation rule |
| --- | --- | --- | --- |
| `source_role` | What authority or evidentiary role does the source have? | Source admission on the `SourceDescriptor`. | Frozen; changing source authority requires a governed descriptor correction/replacement. |
| `knowledge_character` | What epistemic kind is this normalized Atmosphere object? | Normalization/admission review before processed identity closes. | Frozen after identity; re-characterization creates replacement identity and correction lineage. |

A typical mapping may exist, but the relationship is not one-to-one. For example:

- a remote-sensing product may have an observational source role while its object remains `REMOTE_SENSING_MASK`;
- a fusion object may combine observed, modeled, regulatory, and contextual inputs while its output remains `DERIVED_FUSION`;
- a public AQI report may originate from an authoritative agency while remaining `PUBLIC_AQI_REPORT`, not `OBSERVED_SENSOR`;
- a low-cost sensor can be an observed source but still requires the distinct `LOW_COST_SENSOR` character and public-use obligations.

This ADR does not freeze source-role strings from the bounded fixture profile as the canonical source-role vocabulary.

### Required fail-closed behavior

The following conditions must never be silently coerced to a valid character:

| Condition | Minimum internal outcome | Minimum public/API/AI posture |
| --- | --- | --- |
| Missing character | Validation failure and lifecycle `HOLD` or `QUARANTINE` | `ABSTAIN` or omit the unsupported claim |
| Unknown token or alias | Validation failure; no auto-mapping without an accepted compatibility table | `ABSTAIN`; do not guess |
| Multiple characters on one object | Validation failure; require object split or explicit derived/fusion modeling | `ABSTAIN` or `DENY` when the ambiguity could mislead |
| Character contradicts object family, source role, method, or claim | `DENY`/validation failure with stable reason code | `DENY` the collapsed representation |
| Required evidence or time support unresolved | Evidence/release `HOLD` | `ABSTAIN` |
| Rights, sensitivity, or exact-site posture unresolved | Policy `DENY`, `RESTRICT`, generalize, or quarantine | `DENY` or public-safe generalized result |
| Tool, registry, schema, policy, or evidence resolver failure | `ERROR`; no unsafe fallback | `ERROR` |
| Valid character but no review/release state | Remain a candidate; no promotion by implication | No public answer or layer |

`HOLD`, `QUARANTINE`, and `RESTRICT` are internal lifecycle or policy states. Public response envelopes remain governed by their accepted finite-outcome contract, normally `ANSWER | ABSTAIN | DENY | ERROR`.

### Minimum anti-collapse denials

The eventual schema/validator/policy/consumer suite must cover at least:

- `ATMOSPHERIC_MODEL_FIELD` presented as an observation;
- `PUBLIC_AQI_REPORT` presented as concentration;
- `REMOTE_SENSING_MASK` or AOD presented as ground PM2.5;
- `REGULATORY_ARCHIVE` presented as a live current observation without explicit status;
- `LOW_COST_SENSOR` presented as regulatory/reference-equivalent or without required caveats;
- `CLIMATE_ANOMALY_CONTEXT` presented as a current local event observation;
- `DERIVED_FUSION` presented as a direct observation or without per-input lineage;
- `METEOROLOGICAL_CONTEXT` presented as the pollutant or impact claim it supports;
- `ALERT_AND_ADVISORY_CONTEXT` presented as KFM-issued alert or life-safety guidance;
- `NETWORK_AND_SITE_CONTEXT` presented as measurement data or used to expose exact protected coordinates;
- missing, unknown, aliased, or multiple character state;
- a character badge or UI label presented as evidence, policy approval, review, or release state.

Reason codes should be stable, non-echoing, deterministic, and mapped to the accepted decision vocabulary. Current codes may be retained where semantically correct, but acceptance requires an explicit compatibility review rather than assuming fixture identifiers are globally canonical.

### Evidence and time requirements

A character assignment must be inspectable. At minimum, the governed object or resolvable support chain must identify:

- object identity and object family;
- the exact `knowledge_character` token and vocabulary version/digest;
- source descriptor and source role;
- method, product, model, archive, sensor, network, or transformation identity appropriate to the token;
- required observed, issued, valid, forecast, retrieval, baseline, revision, release, or correction times;
- units, spatial support, resolution, and vertical support where applicable;
- `EvidenceRef` values resolvable to an `EvidenceBundle` for consequential claims;
- policy, rights, sensitivity, review, release, and correction references required by the use;
- limitations and uncertainty appropriate to the token;
- replacement/supersession and rollback references after correction.

A schema-valid token without this support is not a supported public claim.

### Derived fusion and cross-domain joins

`DERIVED_FUSION` is not a license to erase input distinctions. A governed fusion or cross-domain join must preserve:

- every material input's source descriptor, source role, and knowledge character;
- transformation identity and `spec_hash` or equivalent deterministic specification reference;
- temporal and spatial compatibility decisions;
- uncertainty and missing-data handling;
- policy and sensitivity effects introduced by the join;
- which claims are source-native and which are derived;
- correction propagation when any input is replaced or withdrawn.

A Hazards, Hydrology, Agriculture, Habitat, public map, or AI consumer must not re-label an Atmosphere input merely because it is convenient for the consuming domain.

---

## Current implementation maturity

Current main contains a meaningful but intentionally narrower implementation than this proposed decision.

### Bounded six-character fixture profile

The executable profile currently recognizes:

```text
OBSERVED_SENSOR
PUBLIC_AQI_REPORT
ATMOSPHERIC_MODEL_FIELD
REMOTE_SENSING_MASK
ALERT_AND_ADVISORY_CONTEXT
NETWORK_AND_SITE_CONTEXT
```

It proves, for synthetic fixture payloads:

- one valid case for each of those six characters;
- exact negative cases for model-as-observation, AQI-as-concentration, AOD-as-ground-PM2.5, advisory-as-life-safety, and precise-site exposure;
- missing, unknown, and multiple-character rejection;
- closed top-level and nested shapes for the fixture profile;
- deterministic sorted findings and bounded input sizes/counts;
- generalized county support rather than exact coordinates;
- no-network execution;
- non-echoing CLI output and finite exit behavior;
- workflow wiring on the Atmosphere domain job.

It does **not** prove:

- acceptance of this eleven-token vocabulary;
- canonical machine-registry placement or content;
- a closed production JSON Schema;
- executable Atmosphere Rego behavior or a bound policy evaluator;
- positive/negative coverage for all eleven proposed tokens;
- source admission or scientific validity;
- live evidence resolution;
- API, MapLibre, Evidence Drawer, export, or AI consumer behavior;
- correction propagation, release, deployment, or publication.

### Values not yet represented by the bounded profile

The current fixture profile has no positive case for:

```text
REGULATORY_ARCHIVE
LOW_COST_SENSOR
CLIMATE_ANOMALY_CONTEXT
DERIVED_FUSION
METEOROLOGICAL_CONTEXT
```

Repository main contains separate bounded work related to some of these concerns, including low-cost-sensor and observed-versus-modeled validation. Those profiles do not automatically expand the knowledge-character fixture enum or prove one unified production contract. Graduation requires deliberate integration and compatibility tests.

### Maturity matrix

| Layer | Current state | Required before implementation graduation |
| --- | --- | --- |
| ADR decision | Unassigned proposed scaffold, modernized by this file | Assign unique ID; reviewed `proposed` ADR; explicit acceptance before binding |
| Human vocabulary | Draft explainer plus thin index | Reconcile wording and index generation/maintenance against the accepted token set |
| Atmosphere semantic contract | Draft and substantive | Update to exact accepted semantics and versioning |
| Cross-domain contract | Draft general pattern | Keep general; explicitly avoid globalizing the Atmosphere enum |
| JSON Schema | Permissive empty-properties scaffold | Closed shape or accepted registry-backed validation with compatibility rules |
| Machine registry | Placeholder in a source-registry lane | Separate placement/authority decision; versioned content and digest |
| Fixture validator | Six-character bounded executable | Deliberately graduate to all accepted values or maintain a clearly versioned subset profile |
| Focused tests | 14 methods; six positive and five file-backed negative fixtures plus in-memory failure states | All-token positive coverage, expanded anti-collapse negatives, compatibility and consumer tests |
| Policy source | Thirteen default-only proposed Rego scaffolds | Accepted input/result contract, package/entrypoint, native tests, bundle, evaluator, consumer binding |
| Evidence closure | Fixture references only | Resolvable evidence chain for consequential real claims |
| API/UI/AI consumers | UNKNOWN | Contract tests showing character preservation, caveats, finite outcomes, and no unsafe fallback |
| Release/correction/rollback | HELD / UNKNOWN | Promotion gate, release manifest, correction propagation, cache invalidation, and rollback drill |

---

## Options considered

### Option A — Closed Atmosphere vocabulary with separate source role and governed enforcement

**Selected.** Adopt the exact eleven-token set, keep `source_role` separate, require exactly one immutable character per governed Atmosphere object, and enforce anti-collapse behavior through the owning roots.

This option is explicit enough for deterministic validation while preserving evidence, policy, release, and domain boundaries.

### Option B — Keep `knowledge_character` as open free text

**Rejected.** Open strings invite spelling variants, hidden aliases, unreviewed new meanings, non-deterministic joins, and incompatible UI/API behavior. They cannot support reliable fail-closed validation or migration.

### Option C — Use `source_role` alone

**Rejected.** Source role describes source authority, not the normalized object's epistemic kind. Remote sensing, public AQI, archives, fusion products, and site metadata demonstrate why one source axis is insufficient.

### Option D — Infer character from object family or source name

**Rejected.** Object families and source products can support more than one epistemic posture. Inference hides the decision, makes corrections difficult, and allows source/product naming to become accidental authority.

### Option E — Make the Atmosphere token set a global cross-domain enum

**Rejected for this ADR.** The cross-domain anti-collapse pattern is valuable, but other domains have their own ubiquitous language and risks. Globalizing these exact tokens would override domain semantics without evidence or an accepted cross-domain decision.

### Option F — Accept only the six tokens implemented by the current fixture profile

**Rejected.** The six-token profile is a bounded proof slice, not a complete domain model. Excluding archives, low-cost sensors, climate context, fusion, and meteorological context would force those records into false categories or ungoverned free text.

### Option G — Allow multiple characters on one object

**Rejected.** Multiple characters make object meaning and identity ambiguous. A composite result should be modeled as `DERIVED_FUSION` with explicit per-input lineage, or split into distinct governed objects.

---

## Consequences

### Positive consequences

- Atmosphere claims carry an explicit, inspectable epistemic type.
- Model, observation, AQI, archive, remote-sensing, advisory, and derivative boundaries become testable.
- Source role remains intact rather than overloaded.
- Schema, policy, validators, API, UI, and AI can converge on finite values and failure outcomes.
- Re-characterization has a visible correction path instead of a silent field edit.
- Cross-domain consumers can preserve input meaning through joins.
- Public surfaces can show caveats appropriate to the product without treating the label as proof.
- The current bounded validator becomes a clear implementation slice rather than accidental vocabulary authority.

### Costs and tradeoffs

- Every relevant Atmosphere object and consumer needs a character field or resolvable reference.
- Existing payloads may need migration, compatibility adapters, or a held state.
- The full token set requires more fixtures, policy tests, consumer tests, and documentation.
- Some records that previously rendered successfully will abstain, deny, quarantine, or remain held.
- Derived fusion and re-characterization require additional lineage and correction objects.
- The machine registry needs a separately governed home and versioning strategy.
- Cross-domain consumers must carry input characters instead of flattening them.

### Risks if implemented poorly

- A closed enum could create false confidence if definitions, evidence, time, and obligations remain vague.
- Duplicate hand-maintained docs and registry files could drift.
- A token could become a UI badge that hides unresolved evidence or release state.
- The current six-token fixture set could be mistaken for the accepted full vocabulary.
- Source-role strings from a synthetic profile could accidentally become canonical.
- A registry placed under a source-specific lane could blur vocabulary authority with source admission.
- Policy could be declared active merely because Rego files exist.
- Re-characterization could overwrite published history rather than issue a correction.
- Cross-domain consumers could silently map unfamiliar tokens to a convenient local class.

---

## Implementation and convergence

This one-file update changes no schema, registry, policy, fixture, validator, test, workflow, API, UI, data, release, or publication behavior. If the candidate receives a unique number and is accepted, implementation should proceed through small, dependency-closed changes.

### Phase 0 — Assign and review the decision

1. Check the canonical ADR index, active branches, and open pull requests for the next collision-free number.
2. Rename this candidate only in a reviewed numbering PR and update `docs/adr/INDEX.md` in the same change.
3. Confirm decision owners and affected stewards.
4. Preserve source status `proposed` until explicit acceptance.
5. Record any conflicts with existing vocabulary, contracts, source-role semantics, and object-family mappings.

### Phase 1 — Reconcile the human and semantic surfaces

1. Align `KNOWLEDGE_CHARACTERS.md` and the Atmosphere semantic contract to the exact eleven tokens and definitions.
2. Keep `KNOWLEDGE_CHARACTER_REGISTRY.md` as a thin index or generated projection, not a competing prose authority.
3. Mark the umbrella phrase as the field/concept, not an enum member.
4. Make cross-domain documentation state explicitly that the token set is Atmosphere-owned.
5. Record supersession or compatibility notes for aliases discovered in existing objects.

### Phase 2 — Decide the machine projection and schema

1. Resolve the machine-registry owning responsibility without promoting the current source-registry placeholder by implication.
2. Create one versioned machine projection with a deterministic digest and no parallel registry.
3. Replace the permissive schema scaffold with a closed or registry-backed shape.
4. Define vocabulary version, token compatibility, required support references, and correction linkage.
5. Add valid/invalid schema fixtures and migration tests.

A machine-registry path that changes or creates authority must be handled by the applicable Directory Rules and ADR process. This candidate does not pre-authorize it.

### Phase 3 — Graduate deterministic fixture enforcement

1. Preserve the current six-token profile as a reproducible baseline.
2. Add positive fixtures for the five unrepresented tokens.
3. Add exact negative fixtures for archives-as-live, low-cost-as-regulatory, anomaly-as-event, fusion-without-lineage, and meteorology-as-primary-claim.
4. Review current reason codes for stable semantic compatibility.
5. Add schema/registry/validator drift tests.
6. Keep fixtures synthetic, generalized, no-network, bounded, and non-echoing.
7. Update or supersede the generated receipt through the legitimate receipt producer.

### Phase 4 — Bind policy and evidence

1. Define one accepted policy input and normalized decision contract.
2. Reconcile duplicate package concepts and `allow`/`deny` result-shape drift.
3. Add native policy tests for character-specific obligations and denials.
4. Build and identify an immutable policy bundle and evaluator binding.
5. Require `EvidenceRef -> EvidenceBundle` resolution where claims depend on evidence.
6. Ensure a valid character never bypasses rights, sensitivity, review, or release gates.

### Phase 5 — Bind governed consumers

1. Add contract tests for governed API payloads.
2. Require Evidence Drawer and exports to disclose character, evidence, time, caveats, and correction state.
3. Require Focus Mode and other AI surfaces to preserve the token and return `ABSTAIN`, `DENY`, or `ERROR` rather than flattening unsupported context.
4. Test map styles and layer manifests so visual similarity does not erase character.
5. Test cross-domain joins and derived fusion with per-input lineage.
6. Confirm no public client reads internal stores or machine registry files directly.

### Phase 6 — Prove correction, release, and rollback

1. Exercise re-characterization as replacement identity plus `CorrectionNotice`, not in-place mutation.
2. Rebuild and verify affected catalog/triplet projections and derived artifacts.
3. Prove cache, search, map, export, and AI invalidation for corrected or withdrawn objects.
4. Require reviewed release manifests and rollback targets.
5. Run a fixture-only release/correction/rollback dry run before any live source or public enablement.

---

## Validation and acceptance gates

### Current validation posture

The current head has successful bounded Atmosphere CI, but this documentation update still requires its own changed-area checks. The recommended commands are:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/atmosphere/test_knowledge_character_registry.py --verbose

python tools/validators/domains/atmosphere/validate_knowledge_character.py \
  fixtures/domains/atmosphere/knowledge_character/valid/*.json

# This command must fail because all inputs are known-invalid.
python tools/validators/domains/atmosphere/validate_knowledge_character.py \
  fixtures/domains/atmosphere/knowledge_character/invalid/*.json
```

Repository-native Markdown, link, metadata, documentation-graph, and changed-area checks should also run through the workflows configured for the pull request. A passing check proves only its declared scope.

### Acceptance gate matrix

| Gate | Current state | Required to accept this ADR |
| --- | --- | --- |
| Same-path candidate | CONFIRMED | Preserve path until reviewed numbering; no duplicate ADR candidate |
| Unique numeric ID | NOT ASSIGNED | Assign collision-free number and update index |
| Decision owners | NEEDS VERIFICATION | Named, accountable decision and domain stewards |
| Exact token set | PROPOSED | Human review of all eleven definitions and exclusions |
| Source-role boundary | SUBSTANTIVE DRAFT | Accepted cross-reference to source-role authority; no vocabulary collapse |
| Human prose/index split | PARTIAL | One prose explainer plus thin/generated index with no competing definitions |
| Semantic contract | SUBSTANTIVE DRAFT | Align exact accepted semantics, versioning, and correction rules |
| Machine registry home | OPEN / CONFLICTED | Separate placement decision and single canonical projection |
| JSON Schema | FAIL / permissive scaffold | Closed or registry-backed validation with compatibility fixtures |
| All-token fixture coverage | PARTIAL, six of eleven | Positive coverage for all accepted tokens |
| Negative anti-collapse coverage | PARTIAL | Full minimum denial matrix and stable reason-code review |
| Policy source | FAIL / default-only scaffolds | Accepted policy input/result contract, native tests, bundle, evaluator |
| Evidence closure | NOT PROVED | `EvidenceRef -> EvidenceBundle` for consequential claims |
| Consumer preservation | UNKNOWN | API/UI/AI/export/cross-domain contract tests |
| Re-characterization | PROPOSED | Replacement identity, correction, supersession, and audit trail |
| Release/correction/rollback | HELD / UNKNOWN | Reviewed dry run and public-client invalidation proof |
| Independent acceptance review | NEEDS VERIFICATION | Review from affected architecture/domain/trust owners |

### Definition of acceptance

This ADR may move from `proposed` to `accepted` only when:

- it has a unique repository-wide ID;
- the canonical ADR index and source status agree;
- all decision owners and required reviewers are identified;
- the exact eleven-token set and semantic boundaries are reviewed;
- relationships to source role, object families, evidence, time, policy, and correction are explicit;
- machine-registry placement is either settled or clearly staged without parallel authority;
- migration and rollback consequences are understood;
- acceptance does not falsely claim implementation or publication.

### Definition of implementation graduation

The implementation may be described as graduated only when:

- the accepted token set has one versioned machine projection;
- the production schema is closed or registry-backed;
- all accepted tokens have positive fixtures and required negative cases;
- validators and policy are deterministic, tested, bounded, and wired to governed consumers;
- source-role and object-family mappings are validated without hidden inference;
- evidence, rights, sensitivity, review, release, correction, and rollback references are enforced where material;
- API, map, UI, export, cross-domain, and AI consumers preserve character and finite outcomes;
- correction and rollback drills pass;
- no live source or public release is implied by the fixture proof.

ADR acceptance and implementation graduation are independent state transitions.

---

## Rollback, correction, and supersession

### Rollback of this documentation change

Before acceptance, rollback is a clean revert of this file to the prior blob. No schema, policy, source, registry, lifecycle, release, or public state is changed by this modernization.

### Rollback after acceptance

An accepted vocabulary cannot be silently removed or edited. A later reversal or material redefinition requires:

- a successor ADR that names this ADR in `supersedes`;
- this ADR marked `superseded` with a forward link;
- token migration and compatibility mapping;
- affected object and consumer inventory;
- correction notices for released objects whose meaning changes;
- regenerated schemas, registries, fixtures, validators, policy, catalogs, and public artifacts;
- cache invalidation and rollback targets;
- retained historical vocabulary versions for audit and replay.

### Character correction

When an individual object's character is wrong:

1. hold or withdraw unsupported downstream claims;
2. preserve the original object and evidence history;
3. create a replacement identity with the corrected character;
4. issue a `CorrectionNotice` or accepted equivalent linking old and new;
5. re-evaluate evidence, policy, review, release, and derived products;
6. invalidate or regenerate affected catalog, map, API, export, search, and AI surfaces;
7. preserve a rollback target and audit receipt.

No correction may rewrite RAW source material or erase the prior released meaning.

---

## Open questions

| ID | Question | Current status | What would settle it |
| --- | --- | --- | --- |
| OQ-01 | What numeric ADR ID should this candidate receive? | OPEN | Concurrent ADR/branch/PR check during a reviewed numbering change |
| OQ-02 | Which named roles are the decision owners and required independent reviewers? | NEEDS VERIFICATION | Project-owner and steward assignment |
| OQ-03 | What responsibility root and exact path owns the machine vocabulary projection? | OPEN / ADR-class if authority changes | Directory Rules placement decision, root-owner review, no-parallel-authority check |
| OQ-04 | Should the thin human registry index be generated from the machine projection? | PROPOSED | Generator design plus stale-output CI test |
| OQ-05 | Which fields are required directly on every domain object versus resolvable through a vocabulary/version reference? | OPEN | Contract and schema review with payload-size and audit tradeoffs |
| OQ-06 | Which source-role values may support each character, and which combinations are denied? | OPEN | Accepted source-role authority plus compatibility matrix |
| OQ-07 | Which object families may carry each token, including role-dependent families? | PARTIAL | Reviewed object-family map and fixtures |
| OQ-08 | How should existing aliases or free-text character fields migrate? | UNKNOWN | Repository-wide payload/fixture/consumer inventory |
| OQ-09 | Which existing validator reason codes become stable compatibility surface? | NEEDS VERIFICATION | Contract, policy, API, and validator review |
| OQ-10 | What public-safe generalization applies to network and site context? | NEEDS VERIFICATION | Sensitivity/policy review and negative tests |
| OQ-11 | What minimum qualification makes low-cost sensor context publicly usable? | NEEDS VERIFICATION | Scientific/source steward decision, policy obligations, synthetic and measured validation |
| OQ-12 | How are per-input characters represented for fusion and cross-domain joins? | OPEN | Derived/fusion contract and schema |
| OQ-13 | Which time kinds are mandatory for each token? | PARTIAL | Alignment with the accepted temporal vocabulary and token-specific contracts |
| OQ-14 | Which current runtime, map, export, and AI consumers already carry or infer character? | UNKNOWN | Commit-pinned consumer inventory and tests |
| OQ-15 | What release and correction drill proves re-characterization propagates safely? | PROPOSED | Fixture-only end-to-end dry run with manifests and rollback |

Unresolved questions remain visible. They are not permission to use free text, invent a mapping, or bypass the fail-closed posture.

---

## Evidence and references

### Governing and repository references

- [`docs/adr/README.md`](./README.md) — ADR lifecycle, naming, inventory, and validation contract.
- [`docs/adr/INDEX.md`](./INDEX.md) — canonical human ADR inventory; this path remains `not-assigned`.
- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) — accepted Directory Rules v2 adoption decision.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — adopted placement bytes.
- [`docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`](../domains/atmosphere/MISSING_OR_PLANNED_FILES.md) — planning source for the original scaffold.
- [`docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../domains/atmosphere/KNOWLEDGE_CHARACTERS.md) — human vocabulary explainer and anti-collapse rationale.
- [`docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md`](../domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md) — thin registry index and open placement record.
- [`contracts/domains/atmosphere/knowledge_character.md`](../../contracts/domains/atmosphere/knowledge_character.md) — draft Atmosphere semantic contract.
- [`contracts/cross_domain/knowledge_character.md`](../../contracts/cross_domain/knowledge_character.md) — draft cross-domain semantic pattern.
- [`schemas/contracts/v1/domains/atmosphere/knowledge_character.schema.json`](../../schemas/contracts/v1/domains/atmosphere/knowledge_character.schema.json) — current permissive machine-shape scaffold.
- [`data/registry/sources/atmosphere/knowledge_character.json`](../../data/registry/sources/atmosphere/knowledge_character.json) — current placeholder, not vocabulary authority.
- [`policy/domains/atmosphere/README.md`](../../policy/domains/atmosphere/README.md) — repository-grounded policy-source boundary and activation hold.
- [`tools/validators/domains/atmosphere/validate_knowledge_character.py`](../../tools/validators/domains/atmosphere/validate_knowledge_character.py) — bounded synthetic fixture validator.
- [`tests/domains/atmosphere/test_knowledge_character_registry.py`](../../tests/domains/atmosphere/test_knowledge_character_registry.py) — focused deterministic tests.
- [`fixtures/domains/atmosphere/knowledge_character/README.md`](../../fixtures/domains/atmosphere/knowledge_character/README.md) — fixture profile and non-authority boundary.
- [`.github/workflows/domain-atmosphere.yml`](../../.github/workflows/domain-atmosphere.yml) — bounded workflow integration and explicit broader hold.
- [`data/receipts/generated/genrec-atmosphere-knowledge-character-fixture-validator-20260802.json`](../../data/receipts/generated/genrec-atmosphere-knowledge-character-fixture-validator-20260802.json) — generated implementation receipt.

### Evidence snapshot identifiers

| Artifact | Identifier |
| --- | --- |
| Base commit | `3e1a929a5e23f570b40c56e473b08ef65c3c5673` |
| Prior target blob | `c101657be0915331693ea1bd8a44a03801bdfbb4` |
| ADR index blob | `938c5894c36b99e14810918e2c550ab0e92d53b1` |
| Accepted ADR-0029 blob | `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` |
| Adopted Directory Rules blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| Knowledge-character schema blob | `9ad7a17e27c349695dd43ce1c48653ae5019f193` |
| Placeholder registry blob | `4b2067e4f1ba70d4689d56ad36b952ead131864c` |
| Fixture validator blob | `6d32922a1f9587df15bcbf040dfe046482fa53cb` |
| Focused test blob | `9d41a7c782e82e4389b80b85b504b146c5d105b0` |
| Fixture README blob | `db59492e001b1b59b60595ad95a854555d753700` |
| Exact-main Atmosphere workflow run | `31825311905` — completed `success` |

No external source or live Atmosphere endpoint was required for this ADR modernization. The decision concerns KFM's internal vocabulary and governance boundaries; source-specific scientific, legal, rights, method, and operational claims remain separate verification work.

---

## Change history

| Date | Change | Decision effect |
| --- | --- | --- |
| Before 2026-08-14 | Tracked five-line `PROPOSED scaffold` sourced from the Atmosphere planned-files register. | None |
| 2026-08-14 | Replaced scaffold in place with a repository-grounded proposed decision, exact token set, anti-collapse semantics, current implementation maturity, convergence plan, acceptance gates, and rollback. | Remains unassigned and proposed; no implementation, release, or publication effect |

### No-loss reconciliation

| Original scaffold element | Disposition |
| --- | --- |
| Existing tracked path | Preserved in place |
| `PROPOSED scaffold` status | Preserved and made explicit as `proposed` / `not-assigned` |
| Source link to `MISSING_OR_PLANNED_FILES.md` | Preserved in Status, Evidence, and References |
| Contract/schema/policy/fixture/release responsibility split | Expanded and aligned with accepted Directory Rules |
| Warning not to treat scaffold as canonical truth | Strengthened into explicit acceptance, implementation, and publication boundaries |

---

> [!IMPORTANT]
> **Decision in one sentence:** Atmosphere objects must say exactly what epistemic kind they are through one closed, immutable, evidence-bound `knowledge_character`; when that state is missing, contradictory, or collapsed, KFM fails closed rather than guessing or publishing a more fluent lie.
