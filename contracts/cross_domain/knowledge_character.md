<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/knowledge-character
title: contracts/cross_domain/knowledge_character.md — KnowledgeCharacter Cross-Domain Contract
type: contract
version: v0.3
status: draft; repository-grounded; domain-preserving; non-publisher
owners: OWNER_TBD — Architecture steward · Atmosphere steward · Source steward · Contract steward · Schema steward · Policy steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
owning_root: contracts/
responsibility: Preserve object-level epistemic meaning across domain boundaries without defining a global enum or replacing domain, schema, registry, policy, evidence, or release authority.
truth_posture: CONFIRMED pinned source inspection; PROPOSED semantic realization; bounded fixture implementation is not production or publication proof.
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@6087d07b49362540e437dc666d1cbaa6eb6b82c3
prior_blob: 4f7eac28c9697c588dd9da35edb29f778fa43aae
policy_label: repository-facing; public-safe-documentation; cross-domain; semantic-contract; source-role-anti-collapse; evidence-aware
related:
  - ./README.md
  - ../domains/atmosphere/knowledge_character.md
  - ../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - ../../docs/adr/ADR-XXXX-atmosphere-knowledge-character-vocabulary.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/domains/atmosphere/knowledge_character.schema.json
  - ../../data/registry/sources/atmosphere/knowledge_character.json
  - ../../tools/validators/domains/atmosphere/validate_knowledge_character.py
  - ../../tools/validators/_common/public_safe_fixture.py
  - ../../fixtures/domains/atmosphere/knowledge_character/README.md
  - ../../tests/domains/atmosphere/test_knowledge_character_registry.py
notes:
  - "Same-path contract-documentation update only. No enum, schema, registry, policy, validator, fixture, workflow, runtime, source admission, or release behavior changes."
  - "The Atmosphere vocabulary names an umbrella term plus eleven specific characters. Its implemented fixture profile covers six, not the full vocabulary and not a global cross-domain enum."
  - "The paired Atmosphere schema is permissive and the machine registry is a placeholder; their presence is not semantic enforcement or accepted registry placement."
  - "This revision preserves document identity and existing headings. Steward assignment, complete vocabulary acceptance, consumer closure, and production enforcement remain open."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KnowledgeCharacter Cross-Domain Contract

> Semantic contract for `knowledge_character`: preserve what kind of knowledge an
> object represents when it crosses a domain boundary. A measurement, model,
> regulatory record, advisory, mask, summary, or fusion product must not silently
> become another kind of evidence.

**Draft semantic contract · Fixture implementation is bounded · No global enum ·
No publication authority**

`contracts/cross_domain/knowledge_character.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema and registry posture](#schema-and-registry-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Atmosphere vocabulary basis](#atmosphere-vocabulary-basis) · [Cross-domain semantics](#cross-domain-semantics) · [Lifecycle](#lifecycle) · [Validation](#validation) · [No-loss preservation](#no-loss-preservation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

The source-inspection checkpoint is
`main@6087d07b49362540e437dc666d1cbaa6eb6b82c3`. Status statements below are
bounded to that commit, not a continuously updated deployment report.

| Surface | Verified posture | What remains outside this evidence |
|---|---|---|
| This cross-domain contract | Existing draft semantic document; same-path revision | Does not assign stewardship, freeze a global vocabulary, or authorize a join |
| Atmosphere domain contract and human vocabulary | Present, draft; domain-specific meaning and anti-collapse requirements | Vocabulary acceptance and complete implementation |
| Atmosphere machine schema | Present, `PROPOSED`, empty `properties`, `additionalProperties: true` | Closed enum, required character, and semantic enforcement |
| Atmosphere machine-registry file | Present, `PROPOSED` placeholder | Accepted registry home, complete values, and operational lookup |
| Atmosphere validator and focused test module | Present executable source for a frozen six-character synthetic profile | Whole-vocabulary coverage, current hosted results, and live consumer enforcement |
| Stewardship, policy, evidence resolution, release, and public use | `NEEDS VERIFICATION` for this contract's complete realization | No approval or operational readiness follows from this document |

Pointers and exact distinctions are in [Schema and registry posture](#schema-and-registry-posture)
and [Validation](#validation). Source inspection is not a test pass. Any local or
hosted execution result must be reported separately with its exact scope and ref.

## Meaning

`knowledge_character` answers: **What epistemic kind does this object represent?**

It is an object-level semantic attribute, not merely display text. The
[Atmosphere explainer](../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
constrains its meaning by source role, evidence, time, and release state. This
cross-domain contract preserves that discipline when consumers cite, compare,
join, derive, display, export, or interpret another domain's objects.

Keep the following concerns separate:

| Concern | Question | Boundary |
|---|---|---|
| Source role | What authority kind does the admitted source represent? | Preserve the source descriptor and its governing vocabulary; do not infer a replacement from a character label |
| Knowledge character | What kind of knowledge does this particular object represent? | Retain the owning domain's meaning and profile/version context |
| Evidence | What admissible support substantiates the claim? | A label or nonempty reference does not resolve `EvidenceRef` to `EvidenceBundle` |
| Policy, review, and release | May this use or exposure proceed? | These require their own decisions; character, schema validity, and fixture success do not grant permission |

The [Atmosphere domain contract](../domains/atmosphere/knowledge_character.md)
owns its domain-specific semantic expectations. This file does not copy that
ownership into a second global authority. It also does not replace
`SourceDescriptor.source_role` or turn an object character into a source catalog.

## Repo fit

The owning responsibility root is `contracts/`: semantic meaning and interface
promises. [Directory Rules](../../docs/doctrine/directory-rules.md), adopted by
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
require shared definitions to be referenced rather than copied (§12.1), and
cross-domain seams to remain under their owning roots (§12.5).

Section 12.5 explicitly uses `contracts/cross_domain/<seam_id>/`. The existing
`cross_domain` container is therefore not merely an unresolved spelling
proposal. This broad semantic file remains at its existing tracked path for
compatibility; this revision does not register it as a seam, choose a new seam
ID, relocate it, or declare every existing descendant path conformant.
Registered-seam mapping or an authority-changing move requires separate
placement and migration evidence.

| Responsibility | Existing reference | Relationship |
|---|---|---|
| Cross-domain navigation | [Directory README](./README.md) | Navigation, not a source of current implementation proof; its June inventory and placement commentary predate this checkpoint |
| Atmosphere meaning | [Domain contract](../domains/atmosphere/knowledge_character.md) | Domain-owned vocabulary-record semantics |
| Human explanation | [Knowledge characters](../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md) | Explainer, rationale, and qualified working glosses |
| Human index | [Registry index](../../docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md) | Thin index; not machine data or an independently writable vocabulary |
| Vocabulary decision | [Unassigned vocabulary ADR](../../docs/adr/ADR-XXXX-atmosphere-knowledge-character-vocabulary.md) | `proposed` / `not-assigned`, not acceptance authority |

No parallel schema, policy, source registry, proof, receipt, release, or public
interface home is created. Older proposed `contracts/<topic>/...` placement
prose must not override the adopted rule.

## Schema and registry posture

The verified machine-shape evidence is the **Atmosphere** schema, not an
established cross-domain KnowledgeCharacter schema.

| Artifact | Current source evidence | Safe interpretation |
|---|---|---|
| [Atmosphere schema](../../schemas/contracts/v1/domains/atmosphere/knowledge_character.schema.json) | Object schema with empty properties, no required character or enum, and additional properties allowed; marked `PROPOSED` | A JSON object can satisfy this scaffold without carrying a valid character; schema validity is not anti-collapse validation |
| [Atmosphere registry placeholder](../../data/registry/sources/atmosphere/knowledge_character.json) | Status, source-document pointer, path, and placeholder note only | Neither a closed vocabulary nor an operational registry; existing source-registry placement does not settle vocabulary authority |
| [Vocabulary ADR candidate](../../docs/adr/ADR-XXXX-atmosphere-knowledge-character-vocabulary.md) | Explicitly unassigned and proposed; distinguishes eleven candidate values from six fixture bindings | Does not accept the enum, fix a global role crosswalk, or authorize release |
| [Bounded fixture validator](../../tools/validators/domains/atmosphere/validate_knowledge_character.py) | Six explicit `FIXTURE_CHARACTER_RULES` entries in Python | Independent fixture-profile checks, not implementation of the permissive schema or an accepted global registry |

A separate cross-domain machine schema, accepted global enum, and operational
registry are **not established by this revision**. This is an evidence limit,
not an exhaustive absence claim. Do not create a second machine home merely to
make the Markdown and directory trees look symmetrical.

The older domain contract and human index retain source-era statements that
validator existence was unverified. The executable source above resolves that
bounded existence question. It does not resolve their vocabulary, registry,
policy, consumer, or release acceptance questions.

## Accepted uses

These are draft semantic uses, not automatic permission to process or publish.

| Use | Contract boundary |
|---|---|
| Describe an object's epistemic kind | Retain the owning domain, vocabulary/profile context, and uncertainty |
| Carry labels across a cross-domain boundary | Preserve each input's character and source role; do not normalize them into assumed equivalents |
| Specify validators and negative cases | Distinguish current fixture checks from proposed full-vocabulary enforcement |
| Display evidence type in an API, map, Evidence Drawer, export, or AI answer | Only through governed, policy-safe, released support with the relevant caveats |
| Support correction review | Preserve prior characterization and affected evidence/consumer lineage |
| Replace source role, prove evidence, accept a vocabulary, or authorize publication | Not permitted by this contract |

## Exclusions

Machine schemas remain in `schemas/`; executable admissibility rules in
`policy/`; validator code in `tools/`; test inputs and executable conformance in
`fixtures/` and `tests/`; governed instances and accountability objects in the
appropriate `data/` lanes; release and correction decisions in their owning
release surfaces. Adopted Directory Rules define those responsibilities.

This contract contains none of the following authorities: a source descriptor,
a machine enum registry, a policy decision, an EvidenceBundle, a proof pack, a
release manifest, a public runtime, or a domain-wide source-role crosswalk.
The existing registry placeholder is not permission to establish one here.

## Recommended fields

The following names are retained as **PROPOSED semantic requirements**, not a
required wire payload. An owning schema/profile must define exact types,
cardinality, identity participation, and versioning before implementation.

| Proposed field | Semantic purpose | Current fixture-profile distinction |
|---|---|---|
| `knowledge_character` | Scoped label for the object's epistemic kind | The Atmosphere fixture accepts exactly one of its six strings, not the full proposed vocabulary |
| `source_role_ref` | Preserve source-role and descriptor basis | The fixture instead carries `source_role` and `source_descriptor_ref`; this is not an alias declaration |
| `evidence_ref` | Support the characterization with admissible evidence | The fixture uses plural `evidence_refs`; nonempty strings are checked but not resolved |
| `time_basis` | Keep observed, issued, valid, retrieval, baseline, and release time distinct where material | No such field or temporal validation is established in this frozen fixture shape |
| `release_caveat` | Carry the caveat required for the intended exposure | Fixture `limitations` are fixed synthetic-profile values, not public release approval |
| `fusion_basis` | Retain every input's character, source role, and lineage | `DERIVED_FUSION` is outside the six-character fixture profile |
| `policy_decision_ref` | Refer to a separate admissibility decision | No live policy evaluation or decision resolution occurs in the profile |
| `review_state` | Preserve qualified review status | Fixture `governance.review_state` is `fixture_only`, not steward approval |

A display label is not an identity token. No new hashing algorithm or universal
identity recipe is selected here. Where characterization participates in
identity or release meaning, follow the owning identity and correction contracts
rather than silently changing the label or regenerating a digest.

## Invariants

A consuming contract must preserve these boundaries; the presence of this list
is not proof that every boundary is currently enforced.

1. Knowledge character is epistemic, not decorative. Preserve domain meaning;
   missing, unknown, or conflicting state fails closed where material.
2. Source role, character, evidence, confidence, policy, review, and release are
   distinct. Neither a label nor a successful fixture check can substitute for
   any of the others.
3. Do not silently edit identity-bearing or release-significant characterization.
   Material re-characterization requires the owning correction/supersession
   procedure, replacement identity where required, provenance, and rollback.
4. Model output is not observation; AQI is not concentration; AOD or a mask is not
   ground PM2.5; regulatory archives retain their vintage; low-cost readings
   retain correction, confidence, limitations, and caveats before public use.
5. Fusion preserves per-input characters and lineage; an advisory reference is
   not KFM life-safety authority; site metadata is not an observed value and must
   not expose protected precision by relabeling it as context.
6. Public and AI surfaces use governed evidence and released artifacts. They
   cite, qualify, abstain, deny, or redirect under their own finite contracts,
   rather than turn character labels or visual plausibility into truth.

## Atmosphere vocabulary basis

The [human explainer](../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
names **twelve terms: the umbrella phrase `Knowledge character` plus eleven
specific characters**. Its working glosses and typical source-role associations
are explicitly **INFERRED guidance**, not verbatim source definitions or an
accepted global mapping. The table below preserves that status.

| Character | Source working gloss and cross-domain caution | Frozen six-character profile |
|---|---|---|
| `OBSERVED_SENSOR` | Instrument reading; do not substitute model, advisory, or aggregate context | Included |
| `PUBLIC_AQI_REPORT` | Agency AQI report; not a concentration | Included |
| `REGULATORY_ARCHIVE` | Regulatory archive/determination; preserve vintage | Not covered |
| `LOW_COST_SENSOR` | Community-grade reading; retain correction, confidence, limitations, and caveats | Not covered |
| `ATMOSPHERIC_MODEL_FIELD` | Model/reanalysis/forecast field; not observation | Included |
| `REMOTE_SENSING_MASK` | Satellite raster, mask, or proxy; not ground PM2.5 | Included |
| `CLIMATE_ANOMALY_CONTEXT` | Baseline-relative context; not a local event or occurrence by itself | Not covered |
| `DERIVED_FUSION` | Multi-source derivative; preserve each input's character and lineage | Not covered |
| `METEOROLOGICAL_CONTEXT` | Supporting meteorology; not automatically the variable it supports | Not covered |
| `ALERT_AND_ADVISORY_CONTEXT` | Advisory/referral context; not KFM alerting authority | Included |
| `NETWORK_AND_SITE_CONTEXT` | Network/site metadata; not observation, and precision remains governed | Included |

“Not covered” means outside **this fixture profile**, not an invalid concept in
all KFM domains. Passing one of those five values to the frozen validator yields
an unknown-character finding; it does not settle the vocabulary proposal.

The exact fixture bindings include lowercase roles such as `observed`,
`regulatory`, `modeled`, `observed_remote_sensing`, and `administrative`.
These local bindings must not be exported as a universal source-role enum or
cross-domain equivalence rule. Keep casing, profile identity, and domain
meaning intact until a separately governed compatibility mapping exists.

## Cross-domain semantics

Knowledge character crosses a boundary when another domain consumes the object
or a derivative. The examples below are semantic requirements, **not claims of
implemented joins, routes, layers, or released products**.

| Proposed use | Required preservation |
|---|---|
| Atmosphere smoke mask used by Hazards | Preserve `REMOTE_SENSING_MASK`; not confirmed fire, observed exposure, or life-safety instruction |
| Atmosphere model field used by Agriculture | Preserve `ATMOSPHERIC_MODEL_FIELD`; not observed field condition or crop truth |
| Climate anomaly used by Habitat/Fauna | Preserve baseline/reference period and `CLIMATE_ANOMALY_CONTEXT`; not per-occurrence evidence by itself |
| Fusion used by Focus Mode | Preserve `DERIVED_FUSION`, per-input characters, source roles, methods, and limitations; narrow or abstain without admissible evidence |
| Advisory reference used by a public UI | Preserve issuing-source and time context; redirect to the official authority rather than issue a KFM alert |

Each endpoint retains its domain-owned facts, evidence support, time, rights,
sensitivity, and correction lineage. A derived output needs its own declared
meaning and provenance; it must not overwrite the inputs' characterization.
Most-restrictive applicable policy and sensitivity obligations survive the
composition. Resolving a reference, matching a cell, or assigning a character
alone does not authorize the relation or its public use.

## Lifecycle

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Character is carried with the governed object; it is not another lifecycle
stage. Source admission establishes the source-role context. The owning domain
contract must determine when object characterization is assigned and frozen.
The Atmosphere explainer refers both to admission and to WORK normalization;
this revision does not invent a universal assignment phase to erase that
wording tension, and the fixture validator tests neither transition.

Before a consequential public claim, the consumer must resolve `EvidenceRef`
to an admissible `EvidenceBundle` and satisfy rights, sensitivity, validation,
provenance, integrity, proof/receipt, policy, review, release, correction, and
rollback obligations. Promotion is a governed transition, not a file move.

Public clients use governed APIs and released artifacts, never internal or
unreleased stores. Maps, tiles, graphs, summaries, and AI carry qualified
interpretations; none creates knowledge-character or evidence authority.
Corrections preserve old and replacement character state and update affected
consumers through the owning correction procedure rather than silent relabeling.

## Validation

### Implemented fixture boundary

The [validator](../../tools/validators/domains/atmosphere/validate_knowledge_character.py)
implements `kfm-atmosphere-knowledge-character-fixture-v1`.
Its [fixture README](../../fixtures/domains/atmosphere/knowledge_character/README.md)
and [focused test module](../../tests/domains/atmosphere/test_knowledge_character_registry.py)
declare six positive JSON cases, five negative cases with exact expected-error
sidecars, and 14 test methods. Missing, unknown, and multiple character cases
are constructed in memory by the tests, not stored as registry entries.

The inspected implementation checks the character's object-family, source-role,
claim-kind, parameter, unit, intended-use, and exact limitation pairing. It
requires bounded, unique, nonempty evidence-reference strings and a nonempty
source-descriptor reference. **It does not resolve those references.**

Spatial support is restricted to `generalized_county` and a five-ASCII-digit
`county_fips`. This checks shape, not the existence of the county, Kansas
membership, real geometry, or the validity of a spatial relationship. Declared
precise-site forms and location aliases are rejected; the profile does not
perform a real-data generalization or sensitivity-adjudication process.

The governance constants remain `fixture_only` rights/review/rollback,
`public_safe_fixture` sensitivity, `not_released` release, and exact boolean
`promotion_eligible: false`. These are fixture constraints, not findings about
real-world rights, approval, or release readiness.

| Negative case | Named finding |
|---|---|
| Model impersonates observation | `MODEL_AS_OBSERVATION_DENIED` |
| AQI impersonates concentration | `AQI_AS_CONCENTRATION_DENIED` |
| AOD impersonates ground PM2.5 | `AOD_AS_PM25_DENIED` |
| Advisory impersonates life-safety guidance | `ADVISORY_AS_LIFE_SAFETY_DENIED` |
| Precise site exposure | `PRECISE_SITE_EXPOSURE_DENIED` |
| Missing / unknown / multiple character | `KNOWLEDGE_CHARACTER_MISSING` / `KNOWLEDGE_CHARACTER_UNKNOWN` / `KNOWLEDGE_CHARACTER_MULTIPLE` |

The [shared fixture helper](../../tools/validators/_common/public_safe_fixture.py)
owns bounded JSON parsing and CLI serialization. Output is **`PASS` or `FAIL`**
with sorted code/path findings; exit codes are `0` for no findings, `1` for
findings, and `2` for missing arguments. A finding ending in `_DENIED` does not
turn that `FAIL` into a PolicyDecision or a public `DENY` response. The separate
API/AI `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` vocabulary is not this CLI's
result enum.

### Reproduction and remaining proof

From a repository checkout containing the pinned implementation and fixtures,
the existing fixture documentation gives this focused command:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/atmosphere/test_knowledge_character_registry.py --verbose
```

The test module explicitly patches selected socket and URL-opening entry points
and asserts no calls for its validation path. `KFM_NO_NETWORK=1` by itself is
not proof of a network sandbox. The command and source inventory are not a
claim that this revision ran the suite or that hosted checks passed.

Full realization still needs accepted vocabulary and registry placement,
non-placeholder schema constraints, proof for all intended characters,
domain-owned source-role compatibility, time and identity/correction tests,
live evidence and policy integration, governed consumer coverage, and release
and rollback evidence. Low-cost-sensor caveats and fusion lineage must not be
reported as covered by this six-character validator.

## No-loss preservation

| Prior element | Disposition |
|---|---|
| Document ID, target path, top anchor, and existing section headings | Retained; no rename or compatibility migration |
| Epistemic/source-role distinction, eleven candidate characters, cross-domain examples | Retained with source qualification and explicit coverage boundaries |
| Machine-shape and registry warnings | Reconciled: actual scaffold/placeholder presence replaces blanket unknowns without claiming acceptance |
| Validator uncertainty | Replaced by verified bounded source inventory; execution and production claims remain separate |
| Identity, evidence, sensitivity, public-use, correction, and rollback controls | Retained; no runtime or authority change |
| Historical scaffold and older evidence ledger | Retained in Git history; no claim that earlier “reviewed” wording proves independent approval |

## Evidence basis

The repository links above were inspected at the immutable checkpoint in
[Status](#status). They support the following separate claims:

| Evidence | Supports | Does not establish |
|---|---|---|
| Prior target blob `4f7eac28c9697c588dd9da35edb29f778fa43aae` | Existing v0.2 semantic content and preservation baseline | An accepted global vocabulary or independent review |
| Accepted ADR-0029 and adopted Directory Rules | Responsibility-root and cross-domain placement law | Vocabulary acceptance or a new seam registration |
| Atmosphere contract, explainer, and human index | Domain meaning, eleven specific terms, source-qualified glosses, and open decisions | Machine enforcement merely through prose |
| Unassigned vocabulary ADR candidate | Explicit proposed scope and six-versus-eleven implementation distinction | Accepted decision or global enum |
| Atmosphere schema and registry placeholder | Their actual limited machine content | Closed vocabulary, reference resolution, or complete registry |
| Validator, shared helper, fixture README, and focused tests | Bounded field checks, finding/CLI semantics, declared fixture inventory, and executable test source | Current test success, live policy/evidence behavior, or release |

Read-only lineage consulted: **KFM Atmosphere / Air PDF-Only Architecture Report
(2026-04-21)**, executive determination and whole-domain architecture; the
Google Drive **Directory Rules** document; and Notion's **KFM Hourly Atmosphere
Domain Builder v1.0** coordination page. The PDF proposes a broader
fourteen-character taxonomy; the repository explainer's eleven specific terms
and the six-code fixture profile are different scopes, not interchangeable
inventories. No extra PDF term is silently admitted here.

The PDF's no-mounted-repository statements describe its historical authoring
session, not this repository. Drive supplies lineage, Notion coordinates work,
and current GitHub bytes establish implementation. None of those source labels
substitutes for adoption, review, validation, or release evidence.

## Rollback

This documentation revision changes no runtime, schema, registry, fixture,
policy, or release object. Before integration, leave the branch unmerged to
withhold the change. After integration, use a separately reviewed forward
revert of this documentation commit; do not rewrite history or automatically
revert unrelated work.

The exact prior-content target is Git blob
`4f7eac28c9697c588dd9da35edb29f778fa43aae` at the inspected base. The earlier
scaffold blob `2669244a79eb46070324196e00346bb2ee41a0eb` is historical lineage,
not the immediate rollback target.

Correct or withdraw this revision if it is used to assert an accepted global
enum, full-vocabulary validation, resolved evidence, policy permission,
independent review, or public release that the evidence does not support.
Rolling back prose does not undo a data correction or a release; those require
their own governed operations.

## Definition of done

This same-path documentation update is distinct from completing the capability.
The capability remains open until:

- [ ] Steward assignments, cross-domain/domain responsibilities, and any needed seam mapping are accepted.
- [ ] Canonical vocabulary values, versions, and machine-registry placement are decided without creating parallel authority.
- [ ] Schema and validator coverage match the intended vocabulary, including the five characters outside the current fixture profile.
- [ ] Source-role compatibility, evidence resolution, temporal semantics, and identity/correction behavior are verified in their owning profiles.
- [ ] Policy and public API/UI/AI consumers preserve caveats, freshness, sensitivity, and fail-closed outcomes with actual tests.
- [ ] Review, release, correction, supersession, and rollback are independently evidenced for any public use.

Safe, reversible documentation and fixture authoring need not wait for those
later capability gates; adopting a vocabulary or publishing claims does.

## Status summary

`knowledge_character` is a domain-preserving epistemic marker, not source role,
EvidenceBundle, schema registry, policy approval, proof of truth, release
permission, or a cosmetic badge. Atmosphere supplies draft vocabulary plus a
real but deliberately bounded six-character fixture implementation. This
contract documents their relationship without promoting either into global or
public authority.

<p align="right"><a href="#top">Back to top</a></p>
